PACKAGE = nanomlwebsite
PY = python
VENV = .env
TENV = .tenv
BIN = $(VENV)/bin
TIN = $(TENV)/bin

all: update_links 

git_docs:
	@cd packages && git submodule add https://github.com/btrainwilson/polytensor.git
	@cd packages && git submodule add https://github.com/nanometaml/mcmc.git

.PHONY: update_links
update_links: $(VENV)
	@echo "Updating links"
	@rm -rf "$(PWD)/docs/source/polytensor"
	@rm -rf "$(PWD)/docs/source/mcmc"
	@cp -r "$(PWD)/packages/polytensor/docs/source" "$(PWD)/docs/source/polytensor" 
	@cp -r "$(PWD)/packages/mcmc/docs/source" "$(PWD)/docs/source/mcmc" 

.PHONY: .env
$(VENV): requirements.txt
	@$(PY) -m venv $(VENV)
	@$(BIN)/pip install --upgrade -r requirements.txt
	@touch $(VENV)

.PHONY: build 
build: $(VENV)
	$(BIN)/python build.py

.PHONY: doc
doc: $(VENV)
	@cd docs && make clean
	@$(BIN)/sphinx-build -M html docs/source docs/build


clean:
	rm -rf $(VENV)
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete

.PHONY: serve
serve: doc
	@$(PY) -m http.server 8018
