#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

# TODO: This won't be "code" anymore
cd /code/app

export POETRY_ENV
POETRY_ENV=$(poetry env info --path)

source "$POETRY_ENV"/bin/activate

python manage.py migrate

"$POETRY_ENV"/bin/daphne -b 0.0.0.0 bells.asgi:application
