FROM python:3.8.11

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "zsh"]
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true

RUN mkdir /logging518

COPY . /logging518
WORKDIR /logging518

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
