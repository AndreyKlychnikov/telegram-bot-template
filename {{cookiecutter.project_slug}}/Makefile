.ONESHELL: all

install:
	@poetry install --no-root

compose:
	@docker-compose up -d

run-local:
	@docker compose up -d db
	@cp compose.env .env
	@export PYTHONPATH=$$PWD:$$PYTHONPATH; \
	poetry run alembic upgrade head; \
	poetry run python app/main.py

migrate:
	@poetry run alembic upgrade head
