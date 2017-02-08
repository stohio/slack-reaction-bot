import os
from slackclient import SlackClient

# TODO wrap this into an initialization class

# get api key
f = open('permissions.txt')
key = f.readline().rstrip()
f.close()

BOT_NAME = 'reactionadder'

slack_client = SlackClient(key)


if __name__ == "__main__":
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
    else:
        print("could not find bot user with the name " + BOT_NAME)

