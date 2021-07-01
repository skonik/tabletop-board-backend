DEV_COMPOSE_FILE_PATH = "./docker/docker-compose.dev.yml"

CI_ENV_FILE = "./dev.env"

# Read .env file and export variables
# Usage example: $(call read_env, $(TEST_ENV_FILE))
define activate_env
	$(shell grep -v "^\#" $(1) | xargs -0) \
	PYTHONPATH=./backend
endef

CI_ENV = $(call activate_env, $(CI_ENV_FILE))

ci.lint:
	poetry run flake8 backend
	$(CI_ENV) poetry run mypy --disallow-untyped-calls --config-file mypy.ini  backend
	poetry run isort backend --check-only


dev.sort:
	isort backend

dev.build:
	docker-compose -f $(DEV_COMPOSE_FILE_PATH) build

dev.up:
	docker-compose -f $(DEV_COMPOSE_FILE_PATH) up  -d --build

dev.down:
	docker-compose -f $(DEV_COMPOSE_FILE_PATH) down --remove-orphans

dev.migrations:
	docker-compose -f $(DEV_COMPOSE_FILE_PATH) run --rm backend ./manage.py makemigrations

dev.migrate:
	docker-compose -f $(DEV_COMPOSE_FILE_PATH) run --rm backend  ./manage.py migrate

# Restart the project using docker-compose
dev.restart:
	docker-compose -f $(DEV_COMPOSE_FILE_PATH) restart backend

dev.ps:
	docker-compose -f $(DEV_COMPOSE_FILE_PATH) ps


dev.logs:
	docker-compose -f $(DEV_COMPOSE_FILE_PATH) logs -f backend


dev.django-shell:
	docker-compose -f $(DEV_COMPOSE_FILE_PATH) run backend  ./manage.py shell

dev.sh:
	docker-compose -f $(DEV_COMPOSE_FILE_PATH) exec backend sh

dev.lint:
	docker-compose -f $(DEV_COMPOSE_FILE_PATH) exec backend flake8 .

dev.test:
	docker-compose -f $(DEV_COMPOSE_FILE_PATH) exec backend pytest
