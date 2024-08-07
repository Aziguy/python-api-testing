# python-api-testing

### install dependencies

> pip install -r requirements-dev.txt

### enable black as a pre-commit hook which will prevent committing not formated source
> pre-commit install

### run black as it will be before each commit
> pre-commit run black

### Create virtual env & install requirements

```sh
virtualenv .venv -p python3
. .venv/bin/activate
pip install -r requirements.txt
```
