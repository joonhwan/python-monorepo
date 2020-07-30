FROM python:3.7-slim

ARG PROJECT_NAME="beam-runner"
ARG POETRY_VERSION=1.0.8
ENV POETRY_VIRTUALENVS_IN_PROJECT=false
ENV POETRY_NO_INTERACTION=1

RUN pip install poetry==$POETRY_VERSION

WORKDIR /app/projects/$PROJECT_NAME

# copy project files
COPY projects/$PROJECT_NAME /app/projects/$PROJECT_NAME
COPY libs /app/libs
#COPY libs /app/projects/$PROJECT_NAME/libs
RUN rm -rf .venv

# install dependency
RUN poetry install --no-dev

# If pip install -e myproject.toml is supported
#RUN poetry export -f requirements.txt > requirements.txt
#RUN pip install -r requirements.txt

ENTRYPOINT ["poetry", "run", "python", "-m", "beam_runner"]
