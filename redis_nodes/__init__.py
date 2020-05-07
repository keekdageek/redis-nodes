
import yaml
from pkg_resources import resource_filename
from logging.config import dictConfig

with open(resource_filename(__name__, f"logging.yml"), 'r') as f:
    dictConfig(yaml.safe_load(f))