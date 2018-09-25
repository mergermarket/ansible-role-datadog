#!/bin/bash

docker run --rm -it \
    -v $(pwd):/${PWD##*/}:ro \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -w /${PWD##*/} \
        retr0h/molecule:latest \
            sudo molecule test
