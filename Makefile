.PHONY: docker_build
docker_build:
	docker build . -t dev

.PHONY: docker_run
docker_run:
	docker run -v $(pwd):/app dev

.PHONY: docker_shell
docker_shell:
	docker run  -it -v $(pwd):/app --entrypoint bash dev