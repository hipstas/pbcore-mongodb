## PBCore-MongoDB setup

```
## Uncomment to kill all currently running Docker containers:
#docker rm -f $(docker ps -aq)

cd /Users/*yourname*/Desktop/pbcore-mongodb/

## Just in case these containers are running already:

docker-compose down

docker-compose build

## Running in detached mode, so we won't get any feedback on the command line. Remove the `-d` argument to see logs and error messages in real time.

docker-compose up -d

docker ps -a
```

Find the image name `pbcoremongodb_web`. Copy the alphanumeric ID in the column to to left, under `CONTAINER ID`.

Swap in that ID in the command below to launch an interactive session in your running image.

```
docker exec -ti  y0ur1Dh3re  /bin/bash
```
