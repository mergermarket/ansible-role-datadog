#!/bin/bash

docker run --rm -it \
    -v $(pwd):/ansible-role-docker:ro \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -w /ansible-role-docker \
        retr0h/molecule:latest \
            sudo molecule --debug test
