FROM python:3.12
LABEL authors="supra"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a new user
# RUN useradd -ms /bin/bash bells
# USER bells

# Upgrade pip, I guess
RUN python3 -m pip install --upgrade pip

# Install Poetry as recommended for CI
ENV POETRY_HOME=/opt/poetry
RUN python3 -m venv ${POETRY_HOME}
RUN ${POETRY_HOME}/bin/pip install poetry==1.4.0
RUN ${POETRY_HOME}/bin/poetry --version

# Copy code?
WORKDIR /code/app/
COPY pyproject.toml poetry.lock /code/app/

# "if local"
COPY --from=django_base . ../django_base

# install Python dependencies
RUN ${POETRY_HOME}/bin/poetry install

ENV PATH="${PATH}:${POETRY_HOME}/bin"

# copy source code
COPY . /code/app/
RUN mkdir /code/app/web/staticfiles

# The celery daemon needs a few other things
COPY celeryd.sh /etc/init.d/celeryd

COPY entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r$//g' /entrypoint.sh
RUN chmod +x /entrypoint.sh

# 0.0.0.0:8000 seems to be important for development
#ENTRYPOINT ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
#ENTRYPOINT ["${POETRY_HOME}/daphne", "-u", "/tmp/daphne.sock", "bells.asgi.application:application"]
