#!/usr/bin/env python
# standard library imports
import logging
import os
import sys

# local imports
from config import config_modes
from slack_shell import setup_logger, LOGGER
from slack_shell.bot.factory import create_bot, run_bot

# Create an instance* of the configuration mode to use,
# so we can access its __repr__ for logging.
#
# * Note the trailing parentheses: '()'
#
# Valid values for `config_modes()` are:
#   'default', 'dev', 'deploy', 'test'
config = config_modes.get(os.getenv('SLACKSHELLBOT_CONFIG', 'default'))()


if __name__ == '__main__':
    setup_logger(config=config)  # initialize application logging
    run_bot(create_bot(config=config))

    if LOGGER:
        LOGGER.info('Shutting down gracefully...')
        logging.shutdown()
    sys.exit(0)