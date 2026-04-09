all: up

up:
	@docker-compose up

down:
	@docker-compose down

check:
	@docker-compose ps

clean: down
	@docker system prune -af

.PHONY: all up down check clean