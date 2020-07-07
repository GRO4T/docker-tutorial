# Based on Docker, FastAPI, Vue.js tutorial
https://medium.com/@bruno.fosados/simple-learn-docker-fastapi-and-vue-js-first-part-docker-setup-a8e4c09ef9c4

#### How to load database credentials from OS environment variables
in docker-compose.yml
```yaml
environment:
      - MONGO_INITDB_ROOT_USERNAME
      - MONGO_INITDB_ROOT_PASSWORD
```
then in the terminal
```bash
$ export MONGO_INITDB_ROOT_USERNAME="tancho_usuer"
$ export MONGO_INITDB_ROOT_PASSWORD="4dm1n4dm1n"
```
#### How to attach to container's terminal
tancho is the name of the Docker container

```bash
docker-compose exec tancho /bin/bash
```

#### Running standalone MongoDB instance using docker
to run
```bash
sudo docker run --name mongo -d -p 27017:27017 mongo
```
to remove all docker containers
```bash
sudo docker rm -f $(docker ps -a -q)
sudo service docker restart
```
to check which containers are currently running
```bash
sudo docker ps
```

#### Project DNS name
EC2Co-EcsEl-QPCLQGLIS95F-65532989.us-west-2.elb.amazonaws.com
