#!/usr/bin/env bash

if [ ! -d "venv/Scripts" ]; then 
  echo "Installing Virtual Environment"
  virtualenv venv
fi

. venv/Scripts/activate
pip install -r requirements.txt

export FLASK_APP=app.py
export DATABASE_URL="postgresql://$(whoami)@localhost/lp02_team_k_server"

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "Starting server <${SCRIPT_DIR}/${FLASK_APP}> ..."
${SCRIPT_DIR}/${FLASK_APP}
