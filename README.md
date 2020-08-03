## Install dependencies
Make sure you install `pipenv`
```bash
pipenv install
```

## Run test
```bash
pipenv run python -m unittest discover -p '*_test.py'
```

## Run script
```bash
pipenv run python main.py | jq
```
