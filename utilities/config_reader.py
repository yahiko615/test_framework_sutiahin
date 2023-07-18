import configparser
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

config_path = os.path.join(current_dir, "..", "configurations", "configuration.ini")

config = configparser.RawConfigParser()
config.read(config_path)


class ReadConfig:

    @staticmethod
    def get_app_base_url():
        return config.get('app_data', 'app_url')

    @staticmethod
    def get_browser_id():
        return config.get('browser_data', 'browser_id')

    @staticmethod
    def get_user_creds():
        return config.get('user_data', 'email'), config.get('user_data', 'password')

    @staticmethod
    def get_app_spell_page_url():
        return config.get('app_data', 'spell_page')

    @staticmethod
    def get_app_spell_page_with_comments():
        return config.get('app_data', 'spell_page_with_comments')

    @staticmethod
    def get_app_login_page():
        return config.get('app_data', 'login_page')

    @staticmethod
    def get_app_dressing_room_page():
        return config.get('app_data', 'dressing_room_page')

    @staticmethod
    def get_app_black_claw_page():
        return config.get('app_data', 'black_claw_page')

    @staticmethod
    def get_app_battle_pet_page():
        return config.get('app_data', 'battle_pet_page')
