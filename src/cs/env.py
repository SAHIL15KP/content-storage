import pathlib
from decouple import Config , RepositoryEnv
from functools import lru_cache


BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
ROOT_DIR = BASE_DIR.parent
ENV_FILE_NAME = ".env"
ENV_BASE_DIR = BASE_DIR / ENV_FILE_NAME
ENV_ROOT_DIR = ROOT_DIR / ENV_FILE_NAME

@lru_cache
def get_config():
    if ENV_BASE_DIR.exits():
        return Config(
            RepositoryEnv(str(ENV_BASE_DIR))
        )
    if ENV_ROOT_DIR.exits():
        return Config(
            RepositoryEnv(str(ENV_ROOT_DIR))
        )
    from decouple import config 
    return config 

config = get_config()