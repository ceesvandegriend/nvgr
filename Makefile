.PHONY: install test lint format build publish

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

publish:
	@echo "+++ Upload +++"
	pdm publish
