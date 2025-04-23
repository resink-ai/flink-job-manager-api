.SHELLFLAGS := -xc
SHELL := /bin/bash
.PHONY: py_21_v1 download release custom_command

# Common variables
SPEC_DIR = spec
CONFIG = $(SPEC_DIR)/gen_config.yaml
YAML_v1 = $(SPEC_DIR)/rest_v1_dispatcher.yml


# Get today's date in YYYYMMDD format
TODAY_DATE := $(shell date '+%Y%m%d')

# Define YAML files as targets that depend on the download action
$(YAML_v1):
	cd $(SPEC_DIR) && bash fetch_and_patch.sh && cd ..

# Download target depends on the YAML files
download: $(YAML_v1)

gen: download
	openapi-python-client generate \
		--path $(YAML_v1) \
		--overwrite \
		--config $(CONFIG)
	cp -v README.md flink-job-manager-api/
	cp -rv spec/py/* flink-job-manager-api/
	poetry -C flink-job-manager-api/ version 1.0.2a$(TODAY_DATE)
	pushd flink-job-manager-api && poetry run pytest tests && popd


release: gen
	cd $$(git rev-parse --show-toplevel)/flink-job-manager-api && poetry run pytest tests
	@if [ $$? -ne 0 ]; then \
		echo "Tests failed. Release aborted."; \
		exit 1; \
	fi
	cd $$(git rev-parse --show-toplevel)
	@echo "Current version:"
	@cat flink-job-manager-api/pyproject.toml | grep version
	@version=$$(cat flink-job-manager-api/pyproject.toml | grep version | cut -d '"' -f2); \
	release_tag="release-$$version"; \
	echo "Tagging and releasing version $$version"; \
	cd $$(git rev-parse --show-toplevel); \
	git add -u; \
	git commit -m "Release version $$version"; \
	git tag -d $$release_tag || true; \
	git tag "$$release_tag"; \
	git push origin "$$release_tag"


release_production: gen
	cd $$(git rev-parse --show-toplevel)
	@echo "setting version to production version 1.0..."
	poetry -C flink-job-manager-api/ version 1.0.2
	$(MAKE) release
