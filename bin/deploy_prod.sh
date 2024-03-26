#!/bin/bash

set -e
set -o xtrace

PROJECT_DIR=/home/techdaysrussia_ru/basket/agroawards2022
PIP=$PROJECT_DIR/venv/bin/pip
PYTHON=$PROJECT_DIR/venv/bin/python
HOST=$(echo $TECHDAYSRUSSIA_PROD_SERVER | cut -d' ' -f1)
PORT=$(echo $TECHDAYSRUSSIA_PROD_SERVER | cut -d' ' -f3)

rsync -e "ssh -p $PORT" -a --progress var/public $HOST:$PROJECT_DIR/tmp/.
set +o xtrace

ssh $TECHDAYSRUSSIA_PROD_SERVER "bash -s" <<EOF
    set -e
    set -o xtrace
    export PATH=$PROJECT_DIR/venv/bin:$PATH;
    cd $PROJECT_DIR;
    git diff --exit-code > /dev/null || $(echo '!!! GIT say: work tree not clean !!!' && exit 1)
    git fetch origin;
    rsync -a --progress $PROJECT_DIR/tmp/public $PROJECT_DIR/var/.
    git checkout $CI_COMMIT_SHA;
    $PIP install -r $PROJECT_DIR/requirements.txt;
    $PYTHON $PROJECT_DIR/back/manage.py migrate --noinput;
    touch $PROJECT_DIR/var/touch

EOF

exit 0
