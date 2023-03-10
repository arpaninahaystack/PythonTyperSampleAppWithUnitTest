import configparser,os
from pathlib import Path

import typer

from appModules.init import appname,SUCCESS ,DIR_ERROR,FILE_ERROR,ERROR

#CONFIG_DIR_PATH = Path(typer.get_app_dir(appname))

CONFIG_DIR_PATH = Path(os.path.dirname(os.path.abspath(__file__)))
CONFIG_FILE_PATH = "config.ini"

def init_app() -> int:
    """Initialize the application."""
    config_code = _init_config_file()
    if config_code != SUCCESS:
        return config_code
    return SUCCESS


def _init_config_file() -> str:
    print("Config dir" + str(CONFIG_DIR_PATH))
    
    if (os.path.exists("config.ini") == False):
        try:
            f = open("config.ini", "w")
            print("File Created")
            return SUCCESS
        except OSError:
            return FILE_ERROR
    else:
        print("File Exists")  
        
        
    return SUCCESS