#! /bin/sh
export FLASK_APP=main
export FLASK_ENV=development
export BUILD=prod #dev, prod, staging
flask run --no-debugger
