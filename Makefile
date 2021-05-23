DEV_COMPOSE_FILE_PATH = "./docker/docker-compose.dev.yml"

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
	docker-compose -f $(DEV_COMPOSE_FILE_PATH) exec backend ./manage.py test