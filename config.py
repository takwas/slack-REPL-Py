# -*- coding: utf-8 -*-
"""
    config
    ~~~~~~

    Configuration for SlackShell.

    :copyright: (c) 2016
    :license: see LICENSE for details.
"""
# standard library imports
import os
import textwrap

# Template string for building string 
# representations for config classes
running_mode = 'App running in {mode} mode. With configs:\n{configs}'


# Base configuration class that will be extended
class Config:
    # Nicks of users who have control over a bot
    BOT_ADMINS = {
        'oxax': 'U0UEMDE04',
        'lekan': 'U0NB51G5T',
        'insaida': 'U0NA6G39N',
        'acetakwas': 'U0NAKE0TT'
    }
    
    SOURCE_URL = 'https://github.com/pyung/slack-shell'
    ABOUT = textwrap.dedent(
                        """
                        A Slack integration that provides a shell for
                        your Slack.
                        Source: {source_url}
                        """.format(source_url=SOURCE_URL)
                        )

    # Log configuration
    LOG_DIR = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), '.logs')
    LOG_FILENAME = 'app_log.log'
    LOG_FORMAT_STR = \
        '\n%(asctime)s - %(name)s - %(levelname)6s: %(message)s'
    
    # Log file rotation scheduling
    
    # Valid values for rotation time:
    #     'S','M','H','D','W0'-'W6','midnight'
    LOG_ROTATION_TIME = 'midnight'
    LOG_ROTATION_INTERVAL = 1  # Don't set to less than 1
    LOG_BACKUP_COUNT = 10  # Don't set to less than 1


# Configuration used during development
class DevConfig(Config):

    DEBUG = True
    TOKEN = os.getenv('SLACKSHELLBOT_TOKEN_DEV', None)
    BOT_NAME = 'slack-shell'
    TEST_CHANNEL = '#bot-test'

    def __repr__(self):
        return running_mode.format(mode='development')


# Configuration used for automated test runs
class TestConfig(Config):

    TESTING = True
    TOKEN = os.getenv('SLACKSHELLBOT_TOKEN_TEST', None)
    BOT_NAME = 'slack-shell'
    TEST_CHANNEL = '#bot-test'

    def __repr__(self):
        return running_mode.format(mode='testing')


# Main configuration used for production
class DeployConfig(Config):

    DEPLOY = True
    TOKEN = os.getenv('SLACKSHELLBOT_TOKEN', None)
    BOT_NAME = 'votebot'  # The nick of the bot.
  
    def __repr__(self):
        return running_mode.format(mode='deploy')


config_modes = {
    'default': DevConfig,
    'dev': DevConfig,
    'deploy': DeployConfig,
    'test': TestConfig
}
