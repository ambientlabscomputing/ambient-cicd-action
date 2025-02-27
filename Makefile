RUN_COMMAND_DOCKER_IMAGE_NAME=run-command-test:latest

.PHONY: build-run-command run-run-command build-and-run
build-run-command:
	docker build -t $(RUN_COMMAND_DOCKER_IMAGE_NAME) .

run-run-command:
	if [ -z $(TOKEN) ]; then \
		echo "Please provide a TOKEN"; \
		exit 1; \
	fi; \
	docker run -it --entrypoint /entrypoint-local.sh -e TOKEN=$(TOKEN) -e API_URL=$(API_URL) $(RUN_COMMAND_DOCKER_IMAGE_NAME)

build-and-run: build-run-command run-run-command
