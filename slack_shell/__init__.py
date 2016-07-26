# -*- coding: utf-8 -*-
import logging
import os
import sys

LOGGER = logging.getLogger(__name__)


def setup_logger(config):
    from logging.handlers import TimedRotatingFileHandler
    global LOGGER

    # Log file rotation scheduling
    when, interval, backupCount = config.LOG_ROTATION_TIME, \
        config.LOG_ROTATION_INTERVAL, config.LOG_BACKUP_COUNT

    # Defensive assertions
    assert when.lower() in ('s', 'm', 'h', 'd', 'midnight',
                            'w0', 'w1', 'w2', 'w3', 'w4', 'w5', 'w6',)
    assert interval > 0
    assert backupCount > 0

    if not os.path.exists(config.LOG_DIR):
        os.mkdir(config.LOG_DIR)
    log_file_path = os.path.join(config.LOG_DIR, config.LOG_FILENAME)

    formatter = logging.Formatter(config.LOG_FORMAT_STR)

    file_handler = TimedRotatingFileHandler(
        log_file_path,
        when=when,
        interval=interval,
        backupCount=backupCount)
    file_handler.setLevel('INFO')
    file_handler.setFormatter(formatter)
    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel('DEBUG')
    console_handler.setFormatter(formatter)
    
    LOGGER.addHandler(file_handler)
    LOGGER.addHandler(console_handler)
    LOGGER.setLevel('DEBUG')

