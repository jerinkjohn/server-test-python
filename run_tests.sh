#!/usr/bin/env bash

if [[ $PATH != *":/venv/bin:"* ]]
then
  echo "Activating Virtual Environment"
  virtualenv venv
  . venv/bin/activate
  pip install -r requirements.txt
fi

export FLASK_APP=app.py
export DATABASE_URL="postgresql://$(whoami)@localhost/lp02_team_k_server"

py.test
