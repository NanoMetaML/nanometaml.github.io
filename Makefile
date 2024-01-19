PACKAGE = nanomlwebsite
PY = python
VENV = .env
TENV = .tenv
BIN = $(VENV)/bin
TIN = $(TENV)/bin

MCMCSRC = $(PWD)/packages/mcmc/docs/source
POLYSRC = $(PWD)/packages/polytensor/docs/source
MCMCBUILD = $(PWD)/docs/source/mcmc
POLYBUILD = $(PWD)/docs/source/polytensor

all: update_links 

git_docs:
	@git submodule update --recursive

.PHONY: doc
doc: $(VENV)
	@cd docs && make clean
	@$(BIN)/sphinx-build -M html docs/source docs/build


.PHONY: .env
$(VENV): requirements.txt
	@$(PY) -m venv $(VENV)
	@$(BIN)/pip install --upgrade -r requirements.txt
	@touch $(VENV)

.PHONY: build 
build: $(VENV)
	$(BIN)/python build.py


clean:
	rm -rf $(VENV)
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete

.PHONY: serve
serve: doc
	@$(PY) -m http.server 8018
