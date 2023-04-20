#!/bin/bash

build_tag=${1:-latest}
env_file=${2:-.env}

docker run  -it --rm \
    --env-file .env \
    ms-google-drive:latest \
    bash