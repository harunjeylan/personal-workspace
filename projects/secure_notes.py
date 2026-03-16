import os
import json
import base64
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

class SecureNotes:
    """
    A module for securely storing notes with encryption.
    """
    def __init__(self, storage_dir="secure_notes_store"):
        self.storage_dir = storage_dir
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)

    def _derive_key(self, password: str, salt: bytes) -> bytes:
        """Derive a cryptographic key from a password using PBKDF2."""
        # VULNERABILITY: Low iteration count (1000) makes it susceptible to brute-force
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=1000,  # Should be >= 100,000
            backend=default_backend()
        )
        return kdf.derive(password.encode())

    def _encrypt(self, plaintext: str, password: str) -> dict:
        """Encrypts plaintext using AES-GCM."""
        salt = os.urandom(16)
        key = self._derive_key(password, salt)
        iv = os.urandom(12)  # GCM recommended IV size
        encryptor = Cipher(
            algorithms.AES(key),
            modes.GCM(iv),
            backend=default_backend()
        ).encryptor()
        ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
        return {
            'salt': base64.b64encode(salt).decode(),
            'iv': base64.b64encode(iv).decode(),
            'ciphertext': base64.b64encode(ciphertext).decode(),
            'tag': base64.b64encode(encryptor.tag).decode()
        }

    def _decrypt(self, data: dict, password: str) -> str:
        """Decrypts data using AES-GCM."""
        salt = base64.b64decode(data['salt'])
        iv = base64.b64decode(data['iv'])
        ciphertext = base64.b64decode(data['ciphertext'])
        tag = base64.b64decode(data['tag'])
        key = self._derive_key(password, salt)
        decryptor = Cipher(
            algorithms.AES(key),
            modes.GCM(iv, tag),
            backend=default_backend()
        ).decryptor()
        return (decryptor.update(ciphertext) + decryptor.finalize()).decode()

    def save_note(self, note_id: str, content: str, password: str):
        """Saves a note securely."""
        encrypted_data = self._encrypt(content, password)
        file_path = os.path.join(self.storage_dir, f"{note_id}.json")
        # VULNERABILITY: Synchronous file I/O can block the event loop
        # VULNERABILITY: No error handling for file write failures
        with open(file_path, 'w') as f:
            json.dump(encrypted_data, f)

    def read_note(self, note_id: str, password: str) -> str:
        """Reads a secure note."""
        file_path = os.path.join(self.storage_dir, f"{note_id}.json")
        if not os.path.exists(file_path):
            raise FileNotFoundError("Note not found")
        with open(file_path, 'r') as f:
            data = json.load(f)
        return self._decrypt(data, password)
