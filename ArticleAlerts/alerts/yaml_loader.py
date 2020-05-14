import yaml


class YamlLoader():

    def __init__(self, input_yaml):
        self.input_yaml = input_yaml

    def load(self):
        with open(self.input_yaml) as file:
            return yaml.load(file, Loader=yaml.FullLoader)