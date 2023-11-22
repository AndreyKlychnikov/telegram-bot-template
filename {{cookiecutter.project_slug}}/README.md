# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

## Installation

Firstly you need to create `.env` file from `compose.env`:
```shell
make init
```
then fill it with your data.


For running app in docker use:
```shell
make compose
```

For running app in development mode use:
```shell
make run-local
```
In this case database is running in a container and app is running locally.

## CI/CD: Github Actions
This GitHub Action template automates the build and deployment of a Docker 
image to a remote server using Ansible.

### Inputs
For proper work of actions you need to specify following secrets for a 
repository. How to specify secrets: [Github docs](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository)

#### `DOCKERHUB_USERNAME`

The username for authenticating with the Docker registry.

#### `DOCKERHUB_TOKEN`

The password or token for authenticating with the Docker registry.

#### `SSH_HOST`

The hostname or IP address of the remote server to deploy the Docker image to.

#### `SSH_PRIVATE_KEY`

The SSH private key used to authenticate with the remote server.

#### `AMPLITUDE_TOKEN`

The token for authenticating with the Amplitude.

#### `TELEGRAM_TOKEN`

The token for authenticating with the Telegram.

#### `SENTRY_DSN`

DSN for sentry integration.

#### `ANSIBLE_PASSWORD`

Password for ansible user.

## Makefile

Makefile has four targets:

- `install`: Installs project dependencies using Poetry.
- `compose`: Starts Docker Compose in detached mode.
- `run-local`: Starts the local development environment using Docker Compose, Alembic for database migration, and Uvicorn for running the FastAPI app. It also copies the `compose.env` file to `.env` for environment variable configuration.
- `migrate`: Runs Alembic migration to upgrade the database to the latest revision.
