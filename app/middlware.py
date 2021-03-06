import docker
import json
from config import InspectorConfig
from constants import CONFIG_NAME, CONFIG_MODE, DOCKER_KEY,DOCKER_MODE_LOCAL, INSPECTOR_PORT

class InspectorMiddlware:
    def __init__(self, path=CONFIG_NAME, mode=CONFIG_MODE):
        self.path = path
        self.mode = mode

        self.iconfig = InspectorConfig(self.path, self.mode)
        self.cli = self._get_docker()

    def _get_docker(self):
        docker_url = self.iconfig.get_config(DOCKER_KEY)

        if docker_url != DOCKER_MODE_LOCAL:
            return docker.Client(docker_url)

        return docker.from_env()

    def images(self):
        images = self.cli.images()

        return json.dumps(images)

    def inspect_image(self, key):
        image = self.cli.inspect_image(key)

        return json.dumps(image)

    def containers(self):
        containers = self.cli.containers()

        return json.dumps(containers)

    def inspect_container(self, key):
        container =  self.cli.inspect_container(key)

        return json.dumps(container)

    def volumes(self):
        volumes = self.cli.volumes()

        return json.dumps(volumes)

    def networks(self):
        networks = cli.networks()

        return json.dumps(networks)

    def inspect_network(self, id):
        network = cli.get("http://{}".format(id))

        return network

    def port(self):
        port = self.iconfig.get_config(INSPECTOR_PORT)

        return int(port)
