import json
import configparser


class ConfigInfo:

    def __init__(self):

        config = configparser.ConfigParser()
        config['DEFAULT'] = {'url': "http://automationexercise.com", 'headless': 'False', 'browser': 'chrome'}
        config['LOGIN'] = {'url': "https://automationexercise.com/login"}

        with open('config.ini', 'w') as config_file:
            config.write(config_file)


    def __read_config(self, section, parameter, config_file = 'config.ini' ):
        config = configparser.ConfigParser()
        config.read(config_file)
        return config.get(section, parameter)


    def get_home_url(self):
        return self.__read_config('DEFAULT', 'url')

    def get_login_url(self):
        return self.__read_config('LOGIN', 'url')