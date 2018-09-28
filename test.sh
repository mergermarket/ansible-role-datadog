#!/bin/bash

role_name=${PWD##*/}

docker run --rm -it \
    -v $(pwd):/$role_name:ro \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -w /$role_name \
        retr0h/molecule:latest \
            sudo molecule test
