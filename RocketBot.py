__author__ = 'eewing'

import socket

class RocketBot:
    server = ""
    channel = ""
    name = ""

    lastuser = ""

    commands = []

    ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, server, channel, name):
        self.server = server
        self.channel = channel
        self.name = name

        self.addcommand("PING :", ping)

    def connect(self):
        print "Connecting to server: " + self.server
        self.ircsock.connect((self.server, 6667))
        self.ircsock.send("USER " + self.name + " " + self.name + " " + self.name + " :This bot is created by Quentillionaire, following a tutorial at http://wiki.shellium.org/w/Writing_an_IRC_bot_in_Python\n")
        self.ircsock.send("NICK " + self.name + "\n")
        self.ircsock.send("JOIN " + self.channel + "\n")
        self.listen()

    def getuser(self, msg):
        try:
            startregex = ':'
            endregex = '!'
            start = msg.find( startregex ) + len(startregex)
            end = msg.find( endregex, start )
            print str(start) + ", " + str(end)
            return msg[start:end]
        except ValueError:
            return ""

    def listen(self):
        while 1:
            ircmsg = self.ircsock.recv(2048)
            ircmsg = ircmsg.strip('\n\r')
            print(ircmsg)

            self.lastuser = self.getuser(ircmsg)
            privstart = ircmsg.find("PRIVMSG ")
            msgstart = ircmsg.find(" :", privstart)
            self.lastmessage = ircmsg[msgstart+2:]

            for command in self.commands:
                if ircmsg.find(command[0]) != -1:
                    command[1](self)


    def sendmsg(self, chan, msg):
        self.ircsock.send("PRIVMSG " + chan + " :" + msg + "\n")

    def addcommand(self, command, func):
        self.commands.append((command, func))

def ping(bot):
    bot.ircsock.send("PONG :Pong\n")