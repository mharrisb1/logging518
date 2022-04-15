FROM python:3.8.11

WORKDIR /logging518
COPY pyproject.toml /logging518

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . /logging518
