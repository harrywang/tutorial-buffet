# About

Setup ClearML server locally on Mac: https://allegro.ai/docs/deploying_trains/trains_server_linux_mac/

Note: I set 6G for Docker

- `docker run hello-world` -- OK
- `sudo mkdir /opt/trains` and then Open the Docker app., On the File Sharing tab, add /opt/trains.

**NOTE: you have to restart docker app after this step!!**
<img width="922" alt="Screen Shot 2020-12-24 at 10 16 29 AM" src="https://user-images.githubusercontent.com/595772/103096194-22d81500-45d1-11eb-906f-877dca676123.png">

- Grant access to the Dockers, depending upon your operating system: `sudo chown -R $(whoami):staff /opt/trains`
- download `sudo curl https://raw.githubusercontent.com/allegroai/trains-server/master/docker-compose.yml -o /opt/trains/docker-compose.yml` to the `/opt/trains` folder.
- run `docker-compose -f /opt/trains/docker-compose.yml up -d`


<img width="1116" alt="Screen Shot 2020-12-24 at 10 42 26 AM" src="https://user-images.githubusercontent.com/595772/103097281-caa31200-45d4-11eb-8c51-e874e9506448.png">

