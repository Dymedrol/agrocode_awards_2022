#!/bin/bash

set -e

PROJECT_DIR=/home/rb/basket/agroawards2022
HOST=$(echo $RB_DEV_SERVER | cut -d' ' -f1)
PORT=$(echo $RB_DEV_SERVER | cut -d' ' -f3)

rsync -e "ssh -p $PORT" -a --progress var/public $HOST:$PROJECT_DIR/tmp/.

ssh $RB_DEV_SERVER "bash -s" <<EOF
    set -e
    set -o xtrace
    export PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games;
    export RUN_SCRIPT=run_uwsgi.sh
    cd $PROJECT_DIR;
    git diff --exit-code > /dev/null || $(echo '!!! GIT say: work tree not clean !!!' && exit 1)
    rsync -a --progress $PROJECT_DIR/tmp/public $PROJECT_DIR/var/.
    git fetch origin;
    git checkout $CI_COMMIT_SHA;

    echo "CONTAINER_TEST_IMAGE=$CONTAINER_TEST_IMAGE" > .env
    docker-compose -f docker-compose.dev.yml -f docker-compose.override.yml down --rmi local --remove-orphans
    docker-compose -f docker-compose.dev.yml -f docker-compose.override.yml build django
    docker-compose -f docker-compose.dev.yml -f docker-compose.override.yml up -d django
    docker-compose -f docker-compose.dev.yml -f docker-compose.override.yml exec -T django prepare_dev_server.sh
    touch ./var/touch

EOF

exit 0
