import configparser
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILES = {'petsqa': BASE_DIR / 'config' / 'petsqa.ini', 'qa': BASE_DIR / 'config' / 'qa.ini'}


def load_config(config_name: str) -> configparser.ConfigParser:
    """
    Loads the configuration from the specified INI file.

    Args:
        config_name (str): The name of the configuration file (without the '.ini' extension).

    Returns:
        configparser.ConfigParser: The loaded configuration.
    """
    config = configparser.ConfigParser()
    config.read(CONFIG_FILES[config_name])
    return config


def get_pet_api_url() -> str:
    """
    Retrieves the API URL for the pet service.

    Returns:
        str: The pet API URL.
    """
    config = load_config('petsqa')
    return config['pet']['url']


def get_store_api_url() -> str:
    """
    Retrieves the API URL for the store service.

    Returns:
        str: The store API URL.
    """
    config = load_config('petsqa')
    return config['store']['url']


def get_flask_app_base_url() -> str:
    """
    Retrieves the base URL for the Flask application.

    Returns:
        str: The Flask app base URL.
    """
    config = load_config('qa')
    return f"http://{config['flaskapp']['url']}:{config['flaskapp']['port']}/api/"


if __name__ == "__main__":
    print(get_pet_api_url())
    print(get_flask_app_base_url())
