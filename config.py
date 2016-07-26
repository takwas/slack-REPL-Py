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

# Configuration used during development
class DevConfig(Config):

    DEBUG = True
    TOKEN = os.getenv('SLACKSHELLBOT_TOKEN_DEV', None)
    BOT_NAME = 'slack-shell'

    def __repr__(self):
        return running_mode.format(mode='development')


# Configuration used for automated test runs
class TestConfig(Config):

    TESTING = True
    TOKEN = os.getenv('SLACKSHELLBOT_TOKEN_TEST', None)
    BOT_NAME = 'slack-shell'

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
