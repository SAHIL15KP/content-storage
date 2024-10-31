import pathlib
from decouple import Config , RepositoryEnv

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
ROOT_DIR = BASE_DIR.parent
ENV_FILE_NAME = ".env"
ENV_BASE_DIR = BASE_DIR / ENV_FILE_NAME

def get_config():
    if ENV_BASE_DIR.exits():
        return Config(
            RepositoryEnv(str(ENV_BASE_DIR))
        )
    from decouple import config 
    return config 

config = get_config()