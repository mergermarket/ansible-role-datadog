#!/bin/bash

role_name=${PWD##*/}

docker run --rm -it \
    -v $(pwd):/$role_name:ro \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -w /$role_name \
        quay.io/ansible/molecule:3.0.2 \
            /bin/sh -c \
            "pip3 install pytest-testinfra; molecule test"
