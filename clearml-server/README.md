# About

Setup ClearML server locally on Mac: https://allegro.ai/docs/deploying_trains/trains_server_linux_mac/

Note: I set 6G for Docker

- `docker run hello-world` -- make sure docker is running correctly
- `sudo mkdir /opt/trains` and then Open the Docker app., On the File Sharing tab, add /opt/trains.

**NOTE: you have to restart docker app after this step!!**
<img width="922" alt="Screen Shot 2020-12-24 at 10 16 29 AM" src="https://user-images.githubusercontent.com/595772/103096194-22d81500-45d1-11eb-906f-877dca676123.png">

- By default, ElasticSearch is mounted at `/opt/trains/data/elastic_7`, you need to create the folder and then give write permission as follows:

```
$ sudo mkdir -p /opt/trains/data/elastic_7
$ chmod 777 /opt/trains/data/elastic_7
```

- Grant access to the Dockers, depending upon your operating system: `sudo chown -R $(whoami):staff /opt/trains`
- download `sudo curl https://raw.githubusercontent.com/allegroai/trains-server/master/docker-compose.yml -o /opt/trains/docker-compose.yml` to the `/opt/trains` folder.
- run `docker-compose -f /opt/trains/docker-compose.yml up -d`

Then go to http://localhost:8080/ to login

<img width="792" alt="Screen Shot 2020-12-25 at 11 26 45 AM" src="https://user-images.githubusercontent.com/595772/103138824-2be5e680-46a4-11eb-810c-65adc477b686.png">

- to restart

```
docker-compose -f /opt/trains/docker-compose.yml down
docker-compose -f /opt/trains/docker-compose.yml up -d
```

