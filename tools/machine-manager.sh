#!/bin/bash

# machine-manager.sh
# A safe wrapper for common machine access tasks.
# Usage: ./machine-manager.sh [command] [args]

COMMAND=$1
shift

case "$COMMAND" in
    "ssh")
        # Wrapper for SSH - ensure you have keys set up
        echo "Connecting via SSH..."
        ssh "$@"
        ;;
    "scp")
        # Wrapper for SCP
        echo "Transferring file via SCP..."
        scp "$@"
        ;;
    "check-disk")
        # Check disk usage safely
        df -h
        ;;
    "check-memory")
        # Check memory usage
        free -h
        ;;
    "list-processes")
        # List running processes (top 10)
        ps aux --sort=-%mem | head -n 11
        ;;
    "log-system")
        # Show recent system logs (last 50 lines)
        journalctl -n 50 --no-pager
        ;;
    "restart-service")
        # Restart a service (requires sudo)
        echo "Restarting service: $1"
        sudo systemctl restart "$1"
        ;;
    *)
        echo "Available commands:"
        echo "  ssh [user@host] [command]"
        echo "  scp [source] [dest]"
        echo "  check-disk"
        echo "  check-memory"
        echo "  list-processes"
        echo "  log-system"
        echo "  restart-service [service-name]"
        exit 1
        ;;
esac
