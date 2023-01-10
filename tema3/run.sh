#!/bin/bash

docker swarm init
docker-compose -f stack.yml build
docker stack deploy -c stack.yml sprc3

docker service logs sprc3_adapter
