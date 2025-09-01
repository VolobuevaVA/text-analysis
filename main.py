import time
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s - %(filename)s - %(lineno)d'
)
logger = logging.getLogger()
while True:
    logger.info("Hello! My name is Valya!")
    time.sleep(20)