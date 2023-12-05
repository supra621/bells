FROM python:3.12
LABEL authors="supra"

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
WORKDIR /code/app
COPY pyproject.toml poetry.lock /code/app/

# "if local"
COPY --from=django_base . ../django_base

# install Python dependencies
RUN ${POETRY_HOME}/bin/poetry install

# copy source code
COPY . /code/app/

ENV PATH="${PATH}:${POETRY_HOME}/bin"

# 0.0.0.0:8000 seems to be important for development
ENTRYPOINT ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
