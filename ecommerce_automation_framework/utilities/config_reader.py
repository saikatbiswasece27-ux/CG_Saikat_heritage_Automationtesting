import configparser
import os


class ConfigReader:
    def __init__(self):
        self.config = configparser.ConfigParser()

        config_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "config",
            "config.ini"
        )

        self.config.read(config_path)

    def get_base_url(self):
        return self.config.get("DEFAULT", "base_url")

    def get_browser(self):
        return self.config.get("DEFAULT", "browser")

    def get_username(self):
        return self.config.get("DEFAULT", "username")

    def get_password(self):
        return self.config.get("DEFAULT", "password")

    def get_implicit_wait(self):
        return self.config.getint("DEFAULT", "implicit_wait")