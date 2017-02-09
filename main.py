#!env/bin/python
import os
import time
from slackclient import SlackClient
from emoji_parser import EmojiParser
from message_parser import MessageParser

# starterbot's ID as an environment variable
BOT_ID = 'U3YLPLY5C'

# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"

# read in the authentication token for bot 
f = open('permissions.txt')
key = f.readline().rstrip()
f.close()

slack_client = SlackClient(key)






"""
Determine which pipeline message should be sent to. 
"""
def determine_message_type(slack_rtm_output):
"""
    Takes the raw slack output an determines if it is a Command or Message type
"""
output_list = slack_rtm_output
if output_list and len(output_list) > 0:
    # print output_list
    for output in output_list:
        # slack output should be parsed as a command
        if output and 'text' in output and AT_BOT in output['text']:
            return 'command'
            return output['text'].split(AT_BOT)[1].strip().lower(), \
            output['channel']

        # slack output should be parsed by NLP engine
        if output and 'text' in output:
            return 'nlp'


return None, None, None, None


if __name__ == "__main__":
    text_parser = EmojiParser(slack_client)
    command_handler = CommandHandler()
    
    READ_WEBSOCKET_DELAY = 0.5 # 1 second delay between reading from data stream
    if slack_client.rtm_connect():
        print("ReactionAdder connected and running!")
        while True:
            msg = slack_client.rtm_read()
            msg_type = determine_message_type(msg)
            if msg_type == 'command':
                command_handler.parse_command(msg) 
            elif msg_type == 'nlp':
                message, channel, timestamp, user = text_parser.parse_message(msg)
                print emoji_list
                for emoji_text in emoji_list:
                    if emoji_text != None: 
                        slack_client.api_call("reactions.add", channel=channel, name=emoji_text, timestamp=timestamp, as_user=True)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")

