#!/bin/bash

printf 'Installing virtualenv\n'
pip3 install virtualenv

printf 'Creating virtualenv\n'
virtualenv env

printf 'Activating created env\n'
# shellcheck disable=SC1091
source env/bin/activate

printf 'Installing dependencies\n'
pip3 install -r requirements.txt

printf 'Run the server\n'
python app.py
