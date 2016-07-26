# local imports
from slack_shell import SlackShellBot, LOGGER


def create_bot(config):
    """Create a Slack bot."""
    if validate_token(config.TOKEN) == False:
        LOGGER.warn('Invalid token provided! Aborting...')
        raise InvalidTokenError

    slack_shell_bot = SlackShellBot(config)
    return slack_shell_bot


def run_bot(bot):
    """Connect bot to server."""
    APP_LOGGER.debug('Running SlackShellBot instance...')
    bot.connect_rtm()
    

def validate_token(token):
    """Confirms that token exists.

    TODO: Should confirm that token meets a specific format.
    """
    if token is None:
        return False


class InvalidTokenError(Exception):
    pass