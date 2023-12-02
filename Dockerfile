FROM python:3.12
LABEL authors="supra"

# Create a new user
# RUN useradd -ms /bin/bash bells
# USER bells

#RUN --mount=source=/Users/supra/PycharmProjects/django_base,destination=/python_local/django_base \
#    ls

#RUN ls

# Upgrade pip, I guess
RUN python3 -m pip install --upgrade pip

# Install Poetry as recommended for CI
ENV POETRY_HOME=/opt/poetry
RUN python3 -m venv ${POETRY_HOME}
RUN ${POETRY_HOME}/bin/pip install poetry==1.4.0
RUN ${POETRY_HOME}/bin/poetry --version

# Copy code?
WORKDIR /code
COPY pyproject.toml poetry.lock /code/

COPY --from=django_base . /python_local/django_base

RUN ${POETRY_HOME}/bin/poetry install

COPY . /code/

ENV PATH="${PATH}:${POETRY_HOME}/bin"


# Start the server?
# 0.0.0.0:8000 seems to be important for development
ENTRYPOINT ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
#ENTRYPOINT ["/bin/sh"]
