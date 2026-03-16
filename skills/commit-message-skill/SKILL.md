---
name: commit-message-skill
description: Helps generate conventional commit messages based on code changes
---

# Commit Message Skill

This skill helps generate clear, conventional commit messages based on the changes made.

## When to Use This Skill

Use this skill when:
- You have finished coding and need to commit
- You want to follow Conventional Commits standard
- You need to generate clear commit messages
- You want to automate commit message generation

## Conventional Commits Format

The skill follows this structure:
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Formatting, missing semicolons, etc.
- **refactor**: Code changes that neither fix a bug nor add a feature
- **perf**: Performance improvements
- **test**: Adding missing tests or correcting existing tests
- **build**: Changes affecting build system or external dependencies
- **ci**: Changes to CI configuration files and scripts
- **chore**: Maintenance tasks
- **revert**: Reverts a previous commit

## How to Use This Skill

### Basic Usage
Ask the skill to generate a commit message:
```
Generate a commit message for these changes:
[describe your changes]
```

### Specific Context
Provide specific details:
```
Generate a commit message for adding user authentication with JWT tokens
```

### Diff-Based Generation
Provide the git diff or describe the changes:
```
Generate a commit message for these git changes:
- Added login endpoint
- Implemented JWT token generation
- Added password hashing
```

## Response Format

The skill provides:
1. **Type**: The commit type (feat, fix, etc.)
2. **Scope**: Optional scope (e.g., auth, api, ui)
3. **Subject**: Short description (50 chars or less)
4. **Body**: Detailed explanation (optional)
5. **Footer**: Breaking changes or issue references (optional)

## Examples

### Feature Addition
```
feat(auth): add JWT token authentication

Implemented secure JWT token generation and validation.
Added password hashing with bcrypt.

Closes #123
```

### Bug Fix
```
fix(api): resolve null pointer exception in user lookup

Fixed issue where looking up non-existent users caused
a null pointer exception. Added proper null checks.

BREAKING CHANGE: User lookup now returns 404 instead of 500
```

### Documentation
```
docs(readme): update installation instructions

Added Docker installation steps and troubleshooting section.
```

## Best Practices

1. **Be Specific**: Use clear, concise language
2. **Use Present Tense**: "Add feature" not "Added feature"
3. **Capitalize First Letter**: Start with a capital letter
4. **No Period at End**: Subject line should not end with a period
5. **Limit Subject Line**: 50 characters or less
6. **Wrap Body at 72 Characters**: For readability
7. **Use Body for Context**: Explain what and why, not how

## Integration with Git

This skill works well with:
- `git commit -m "message"`
- Pre-commit hooks
- CI/CD pipelines
- Code review workflows

## Tips for Effective Commit Messages

1. **One Commit per Logical Change**: Don't mix unrelated changes
2. **Reference Issues**: Link to tickets or issues
3. **Explain Why**: Not just what changed
4. **Use Imperative Mood**: "Add feature" not "Adds feature"
5. **Review Before Commit**: Ensure message accurately reflects changes
