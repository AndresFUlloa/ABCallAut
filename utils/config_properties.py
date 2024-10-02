import json
import os


class ConfigProperties:
    def __init__(self, config_file='config.json'):
        self.project_path = os.path.dirname(os.path.dirname(__file__))
        self.config_file = config_file
        self.config_data = self._load_config()

    def _load_config(self):
        config_path = os.path.join(self.project_path, self.config_file)
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found: {self.config_file}")

        with open(config_path, 'r') as file:
            return json.load(file)

    def get(self, key, default=None):
        return self.config_data.get(key, default)

    def get_home_url(self):
        return self.get('home_url')
