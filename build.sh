#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py loaddata dados_iniciais.json

if [ -f "dados_iniciais.json" ]; then
    python manage.py loaddata dados_iniciais.json || true
fi