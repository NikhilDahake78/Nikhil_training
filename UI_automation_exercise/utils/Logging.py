import logging
import argparse

class log:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        # logging.basicConfig(**self.log_config)

    def title(self, msg):
        self.logger.info("")
        self.logger.info("######################################################")
        self.logger.info(f"\t\t\t  {msg}")
        self.logger.info("######################################################")
        self.logger.info("")

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

    def warning(self, msg):
        self.logger.warning(msg)

Log = log()