#!/bin/bash

set -e
set -o xtrace

python ./manage.py migrate
python ./manage.py loaddata core/fixtures_dev/*
#python ./manage.py collectstatic --no-input
