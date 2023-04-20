#!/bin/bash
set -e

# Run any custom scripts
if [ -d scripts/docker-entrypoint.d ]; then
    for f in scripts/docker-entrypoint.d/*.sh; do
        echo "Executing $f"
        [ -f "$f" ] && . "$f"
    done
fi

# exec the given arguments
exec "$@"
