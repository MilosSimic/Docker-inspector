import yaml
from constants import CONFIG, DOCKER_KEY, INSPECTOR_PORT

class InspectorConfigMap:
    def __init__(self):
        self.map = {}
        self.map[DOCKER_KEY] = 0
        self.map[INSPECTOR_PORT] = 1

    def get(self, key):
        return self.map[key]


class InspectorConfig:
    def __init__(self, path=None, mode=None):
        self.path = path
        self.mode = mode

        self.map = InspectorConfigMap()
        self.cfg = self._load_yaml()

    def _load_yaml(self):
        cfg = None
        with open(self.path, self.mode) as f:
            cfg = yaml.load(f)

        return cfg

    def get_config(self, key):
        i = self.map.get(key)
        return self.cfg[CONFIG][i][key]

    def config(self):
        return self.cfg
