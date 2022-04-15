FROM python:3.8-bullseye

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get -y install gnupg \
    software-properties-common \
    apt-transport-https \
    ca-certificates \
    curl \
    zsh \
    jq 

# gcloud
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
RUN apt-get update && \
    apt-get -y install google-cloud-sdk

# oh-my-zsh
RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Build dbt environment
RUN pip3 install poetry
WORKDIR /logging518
COPY pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .
