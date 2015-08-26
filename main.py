__author__ = 'eewing'

import RocketBot
import Commands
server = "irc.freenode.net"
#channel = "#RocketTourney"
channel = "#rtbot_test"
nickname = "RT_Bot1"

bot = RocketBot.RocketBot(server, channel, nickname)

# Add commands here
bot.addcommand("!test", Commands.firstcommand)
bot.addcommand("!echo", Commands.echo)
bot.addcommand("!bracket", Commands.showbracket)

bot.connect()