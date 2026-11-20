#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 1 ]; then
    echo "Uso: actualizar-proyectos <archivo.ods|archivo.xlsx>" >&2
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY_SCRIPT="$SCRIPT_DIR/actualizar_proyectos.py"

python3 "$PY_SCRIPT" "$1"
