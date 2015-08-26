__author__ = 'eewing'

import RocketBot

def firstcommand(bot):
    bot.sendmsg(bot.channel, "Testing dynamic command loading")

def showbracket(bot):
    bot.sendmsg(bot.channel, "You can see the bracket at http://challonge.com/RLOpen2015")

def startmatch(bot):
    bot.sendmsg(bot.channel, "Match starting!")

def echo(bot):
    bot.sendmsg(bot.channel, bot.lastmessage)