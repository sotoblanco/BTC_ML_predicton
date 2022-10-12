import logging
import logging.handlers
from datetime import datetime

from data.get_binance import *
from data.feature_creation import *

# for github actions and to store the logs
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

if __name__ == "__main__":

    try:
        store_data()
        feature_engineering()
        logger.info('Data store succesfully')
    except:
        logger.info("No data available")
