all: up

up:
	@docker-compose up

down:
	@docker-compose down

clean: down
	@docker system prune -af

.PHONY: all up down clean