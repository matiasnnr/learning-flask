#!/bin/bash

# source venv/bin/activate
venv/Scripts/activate

pip install -r requirements.txt
pip freeze > requirements.txt

export FLASK_APP=main.py
export FLASK_DEBUG=1
export FLASK_ENV=development

flask run