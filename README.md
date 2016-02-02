[Fabric](http://www.fabfile.org/) script for automating various tasks on the Raspberry Pi.


### Usage

```
fab --hosts=ip_or_hostname_for_pi name_of_task
```

### Tasks

* `update_upgrade` - Performs `sudo apt-get update` then `sudo apt-get upgrade -y`.
* `reboot` - Reboot
* `halt` - Halt
* `install_node:node_version:pi_version` - Download and install [Node.js](https://nodejs.org). `node_version` is the version of Node.js to install. Example: `4.2.6`. `pi_version` is the version of the Raspberry Pi board. Use a `2` for the [Raspberry Pi 2 Model B](https://www.raspberrypi.org/products/raspberry-pi-2-model-b/), otherwise leave blank for older boards.

### Docker

This project includes a [Dockerfile](https://docs.docker.com/engine/reference/builder/) and [docker-compose.yml](https://docs.docker.com/compose/compose-file/) to use this project without having to install Fabric locally.

```
docker-compose run fab --hosts=ip_or_hostname_for_pi name_of_task
```
