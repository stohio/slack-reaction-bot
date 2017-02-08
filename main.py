#!env/bin/python
import os
import time
from slackclient import SlackClient
from emoji_parser import Emoji

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


class MessageParser:




def parse_slack_output(slack_rtm_output):
    """
        Takes the raw slack output an determines if it is a Command or Message type
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        # print output_list
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                output['channel']

            if output and 'text' in output:
                # return text after the @ mention, whitespace removed
                return output['text'], \
                       output['channel'], \
                       output['ts'], \
                       output['user']


    return None, None, None, None


if __name__ == "__main__":
    text_parser = Emoji(slack_client)
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("ReactionAdder connected and running!")
        while True:
            text, channel, timestamp, user = parse_slack_output(slack_client.rtm_read())
            if text and channel and timestamp and user != BOT_ID:
                message = text_parser.format_text(text)
                emoji_list = text_parser.search_list(message.split())
                print emoji_list
                for emoji_text in emoji_list:
                    if emoji_text != None: 
                        slack_client.api_call("reactions.add", channel=channel, name=emoji_text, timestamp=timestamp, as_user=True)
#                        del emoji_list[:]
#                        del text
#                        del channel
#                        del timestamp
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")

