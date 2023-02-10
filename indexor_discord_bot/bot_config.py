import configparser
import os


class DictToObjAccess:

    def __init__(self, props: dict):
        self.props = props

    def __getattr__(self, item):
        if item not in self.props:
            return None

        if type(self.props[item]) is dict:
            return DictToObjAccess(self.props[item])

        return self.props[item]


class BotConfig(DictToObjAccess):

    def __init__(self, config_path: str):
        self.path = config_path
        self.parser = configparser.ConfigParser()

        if not os.path.exists(config_path):
            return

        self.parser.read(config_path)

        self.parser.sections()

        parsed_dict = {s: dict(self.parser.items(s)) for s in self.parser.sections()}

        super().__init__(parsed_dict)

