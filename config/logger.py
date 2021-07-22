import logging
import sys
import os

LOGGER = logging.getLogger(__name__)


def prepare_dirs_loggers(config, script):
    logFormatter = logging.Formatter("%(message)s")
    rootLogger = logging.getLogger(script)
    rootLogger.setlevel(logging.DEBUG)

    consoleHandler = logging.StreamHandler(sys.stdout)
    consoleHandler.setLevel(logging.DEBUG)
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)

    if hasattr(config, 'forward_only') and config.forward_only:
        return

    fileHandler = logging.FileHandler(os.path.join(config.saved_path, 'session.log'))
    fileHandler.setlevel(logging.DEBUG)
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def logging_FileHandler():
    pass


logger_handler = logging_FileHandler('python_logging.log')
logger_handler.setLevel(logging.INFO)
logger_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
logger_handler.setFormatter(logger_formatter)
logger.addHandler(logger_handler)
logger.info('Logging setting finished!')
