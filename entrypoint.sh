#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

cd /code/app

export POETRY_ENV
POETRY_ENV=$(poetry env info --path)

source "$POETRY_ENV"/bin/activate

python manage.py migrate

#celery -A bells worker -l INFO --detach
#python manage.py runserver 0.0.0.0:8000
"$POETRY_ENV"/bin/daphne -b 0.0.0.0 bells.asgi:application
