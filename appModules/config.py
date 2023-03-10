import configparser
from pathlib import Path

import typer

from appModules.init import appname,SUCCESS ,DIR_ERROR,FILE_ERROR,ERROR

CONFIG_DIR_PATH = Path(typer.get_app_dir(appname))
CONFIG_FILE_PATH = CONFIG_DIR_PATH/"config.ini"

def init_app() -> int:
    """Initialize the application."""
    config_code = _init_config_file()
    if config_code != SUCCESS:
        return config_code
    return SUCCESS


def _init_config_file() -> str:
    try:
        CONFIG_DIR_PATH.mkdir(exist_ok=True)
    except OSError:
        return DIR_ERROR
    try:
        CONFIG_FILE_PATH.touch(exist_ok=True)
    except OSError:
        return FILE_ERROR
    return SUCCESS