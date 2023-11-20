# Cookiecutter Readme

This is a [Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/) 
template for starting a new project with predefined configurations and file 
structures. The template includes settings for a Telegram bot application with a 
PostgreSQL database and deployment scripts(Github Actions).

## Usage

To use this template, you will need to have Cookiecutter installed. If you don't have it installed, you can install it with the following command:

```
pip install cookiecutter
```

Once Cookiecutter is installed, you can generate a new project using this template with the following command:

```
cookiecutter gh:AndreyKlychnikov/telegram-bot-template
```

You will be prompted to provide values for template.

## Variables

The following variables are used in this template:

- `project_name`: The name of your project.
- `project_slug`: The name of your project, with spaces replaced with 
hyphens and all lowercase.
- `project_short_description`: A short description of your project.
- `on_bot_start_message`: The message that will be sent to the user when he executes the /start command.
- `on_bot_help_message`: The message that will be sent to the user when he executes the /help command.
- `postgres_db`: The name of the PostgreSQL database.
- `postgres_user`: The username for the PostgreSQL database.
- `postgres_password`: The password for the PostgreSQL database.
- `docker_registry_url`: The URL of the Docker registry you will use to host 
your Docker image.
- `docker_image_name`: The name of the Docker image for your project. E.g. your_username/image_name
- `deploy_branch`: The name of the branch you will use for deployment.
- `vps_host`: The IP address of your VPS.
- `vps_user`: The username for your VPS.
- `_copy_without_render`: A list of files and directories that should be 
copied to the new project without being rendered.

## Project Structure

The generated project will have the following structure:

```
project/
├── .github/
│   └── workflows/
│       └── deploy_backend.yml          # Workflow for building & deploying the backend
├── ansible/
│   ├── deploy.yml                      # Ansible playbook for deploying the app
│   ├── hosts                           # Ansible inventory file with the list of hosts
│   └── tasks/
│       ├── compose.yml                 # Ansible task for deploying the app with Docker Compose
│       └── docker_login.yml            # Ansible task for logging in to the Docker registry
│   └── templates/
│       └── docker-compose.yml.j2       # Jinja2 template for Docker Compose configuration file
├── app/                                # Main application directory
│   ├── alembic/                        # Alembic directory for database migrations
│   │   ├── README
│   │   ├── script.py.mako
│   │   └── versions/                   # Directory for storing Alembic migration scripts
│   │       └── ad362c343940_initial.py # Initial migration script
│   ├── core/                           # Core directory
│   │   └── config.py                   # App configuration module
│   ├── db/
│   │   ├── base.py                     # Module with all models(needed for alembic)
│   │   ├── base_class.py               # Base class for SQLAlchemy models
│   │   ├── init_db.py                  # Script for initializing the database
│   │   └── session.py                  # SQLAlchemy session management module
│   ├── handlers/                       # Telegram handlers directory
│   │   └── base.py                     # Base handlers: start, help, etc.
│   ├── main.py                         # Entry point for the app
│   ├── models/                         # Models directory
│   │   └── base.py                     # Base models
│   ├── services/                       # Telegram handlers directory
│   │   ├── analytics.py                # Analytics service (amplitude)
│   │   └── storage.py                  # Storage service, database usecases
│   └── tests/                          # Tests directory
├── .pre-commit-config.yaml             # Pre-commit hooks
├── Dockerfile                          # Dockerfile for building the app container image
├── README.md                           # Readme file with the project description and instructions
├── docker-compose.yml                  # Docker Compose configuration file for local development
├── pyproject.toml                      # Poetry configuration file with project dependencies
└── setup.cfg
```


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