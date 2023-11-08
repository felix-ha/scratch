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

.PHONY: start_frontend
start_frontend: ## TODO working directory of container must be app/
	docker build -t python-server .
	docker run -d -p 8501:8501 python-server streamlit run frontend/main.py
	