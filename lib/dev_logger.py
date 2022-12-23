import logging
import sys

DEBUG_LEVEL_NUM = 9


class Dev_Logger:
    def __init__(self) -> None:
        """

        """

        self.debug_name = "DEBUGV"
        logging.basicConfig(
            stream=sys.stderr, level=logging.DEBUG)

    def enableDebug(self):
        logging.addLevelName(DEBUG_LEVEL_NUM, self.debug_name)

    def isEnabledFor(self, level_num: int):
        log = logging.getLevelName(level_num)
        return log == self.debug_name

    def debug(self, text: str):
        if self.isEnabledFor(DEBUG_LEVEL_NUM):
            logging.debug(f' {text}')
            # logging.debug(text)

    def info(self, text: str):
        logging.info(f' {text}')

    def warning(self, text: str):
        logging.warning(f' {text}')

    def error(self, text: str):
        logging.error(f' {text}')

    def exception(self, text: str):
        logging.exception(f' {text}')
