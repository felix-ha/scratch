.PHONY: docker_build
docker_build:
	docker build -t python-server . 

.PHONY: docker_run
docker_run:
	docker run -d -p 5000:5000 python-server