import yaml

class InspectorConfig:
    def __init__(self, path='config.yml', mode='r'):
        self.path = path
        self.mode = mode

        self.cfg = self._load_yaml()

    def _load_yaml(self):
        cfg = None
        with open(self.path, self.mode) as f:
            cfg = yaml.load(f)

        return cfg

    def get_config(self, key):
        return self.cfg['config'][key]

    def config(self):
        return self.cfg
