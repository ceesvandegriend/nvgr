.PHONY: install test lint format build upload

install:
	@echo "+++ Install +++"
	test -d __pypackages__ || mkdir __pypackages__
	pdm install -d

test:
	@echo "+++ Test +++"
	pdm test

lint:
	@echo "+++ Lint +++"
	pdm lint

format:
	@echo "+++ Format +++"
	pdm format

build:
	@echo "+++ Build +++"
	pdm build

upload:
	@echo "+++ Upload +++"
	pdm upload
