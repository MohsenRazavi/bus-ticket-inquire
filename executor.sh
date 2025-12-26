#!/usr/bin/env bash
source ENV

LOG_FILE="$PROJECT_DIR/cron.log"

cd "$PROJECT_DIR" || exit 1

"$VENV_PYTHON" -m app.main >> "$LOG_FILE"
