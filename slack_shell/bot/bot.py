# standard library imports


# third-party library imports
from slackclient import SlackClient

# local imports
from .parser import Parser
from slack_shell import LOGGER


class SlackShellBot(SlackClient):
    """A Slack bot interface to the Slack shell engine/integration.

    Init:
        :Args:
            config (obj): A configuration instance for the bot.
    """

    # Create bot instance
    def __init__(self, config):
        SlackClient.__init__(self, config)
        self.config = config
        self.username = config.BOT_NAME
        self.admins = config.BOT_ADMINS
        self.sourceURL = config.SOURCE_URL
        self.about = config.ABOUT
        self.parser = ArgsParser(bot=self)
        self.current_channel = None
        

    # Connect to Slack's RTM API
    def connect_rtm(self):
        '''
        Connects to the RTM Websocket

        :Args:
            None

        :Returns:
            None
        '''
        LOGGER.debug('SlackShellBot connecting to RTM API...')
        if self.rtm_connect():
            LOGGER.info('SlackShellBot connected!')
        else:
            LOGGER.warn('SlackShellBot failed to connect!')