FROM python:3.12-alpine

WORKDIR /opt

COPY poetry.lock pyproject.toml ./

RUN pip install poetry \
    && poetry config virtualenvs.create false\
    && poetry install --no-root

COPY . .

ENTRYPOINT sh entrypoint.sh
