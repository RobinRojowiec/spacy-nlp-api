docker stack remove nlp_api
docker-compose build
docker-compose push
docker stack deploy --compose-file docker-compose.yml nlp_api
