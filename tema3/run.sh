#!/bin/bash

cp provisioning $SPRC_DVP -r

docker swarm init
docker-compose -f stack.yml build
docker stack deploy -c stack.yml sprc3
