# Graphql App
App using django & graphql

# note
if docker-compose.yml or Dockerfile is changed,
	retyping "docker-compose build"
	and "docker-compose up -d" to run in deamon
#
docker-compose run DOCKER_COMPOSE_SERVICE sh -c "COMMAND"
> docker-compose run app sh -c "python3 manage.py migrate && python3 manage.py runserver"
#
docker run -it IMAGE_ID COMMAND
> docker run -it 1234 bash
#
docker exec -it CONTAINER_ID COMMAND
> docker exec -it 1234 bash
#
using docker-compose --rm for services run once, avoid to linger on a system after it's ran
> docker-compose run app --rm 
