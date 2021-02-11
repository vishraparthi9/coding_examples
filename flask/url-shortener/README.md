

## Requirements

```
pip3 install pipenv
pipenv install
pipenv shell - to login to the shell
```

## Run

Run the below command to specify what app to run (below example, `hello` is the app):
```
export FLASK_APP=hello
```

In order to immediately see the changes to the code, set the following (default is production):
```
export FLASK_ENV=development
```