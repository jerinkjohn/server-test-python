#!/usr/bin/env bash

if [ ! -d "venv/Scripts" ]; then 
  echo "Installing Virtual Environment"
  virtualenv venv
fi

. venv/Scripts/activate
pip install -r requirements.txt


export FLASK_APP=app.py
export DATABASE_URL="postgresql://$(whoami)@localhost/lp02_team_k_server"

py.test
