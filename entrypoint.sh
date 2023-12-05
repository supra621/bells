#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

source "$(poetry env info --path)"/bin/activate

python manage.py migrate

#celery -A bells worker -l INFO --detach

python manage.py runserver 0.0.0.0:8000
