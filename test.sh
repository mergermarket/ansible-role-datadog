#!/bin/bash

role_name=${PWD##*/}

docker run --rm -t \
    -v $(pwd):/$role_name:ro \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -w /$role_name \
        mergermarket/ansible-molecule:latest \
            /bin/sh -c \
            "pip3 install pytest-testinfra; molecule test"
