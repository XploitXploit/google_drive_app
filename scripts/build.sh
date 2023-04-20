#!/bin/bash

build_tag=${1:-latest}

export DOCKER_BUILDKIT=1
docker build -t ms-google-drive:$build_tag -f Dockerfile .