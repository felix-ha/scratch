.PHONY: docker_build
docker_build:
	docker build -t python-server . 

.PHONY: docker_run
docker_run:
	docker run -d -p 8000:8000 python-server

.PHONY: start_server
start_server:
	docker compose up -d --build python-server

.PHONY: stop_server
stop_server:
	docker compose down python-server
	