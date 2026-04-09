all: up

up:
	@docker-compose up

down:
	@docker-compose down

start:
	@docker-compose start

stop:
	@docker-compose stop

clean: down
	@docker system prune -af

.PHONY: all up down start stop clean