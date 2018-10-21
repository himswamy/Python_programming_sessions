import logging.config
import yaml
from src.config.config import PROJECT_DIR


class loggenerate:

    def __init__(self):
        with open(PROJECT_DIR + '/src/exception/log.yml', 'r') as stream:
            config = yaml.load(stream)
        logging.config.dictConfig(config)
        self.logger = logging.getLogger("simpleExample")
