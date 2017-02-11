from slackclient import SlackClient

"""
Handle all commands
"""
class CommandHandler:
    BOT_ID = 'U3YLPLY5C'
    AT_BOT = "<@" + BOT_ID + ">"

    def __init__(self, slack_client):
        self.slack_client = slack_client

    """
    Decides what type of command was given. 
    """

    def get_command_info(self, slack_rtm_output):
	"""
	    The Slack Real Time Messaging API is an events firehose.
	    this parsing function returns None unless a message is
	    directed at the Bot, based on its ID.
	"""
	output_list = slack_rtm_output
	if output_list and len(output_list) > 0:
	    for output in output_list:
		if output and 'text' in output and self.AT_BOT in output['text']:
		    # return text after the @ mention, whitespace removed
		    return output['text'].split(self.AT_BOT)[1].strip().lower(), \
			   output['channel']
	return None, None

    def parse_command(self, word_list, channel):
        print(word_list, channel)
        if word_list[0].lower() == 'add':
            print("adding a new synonym....")
            # self.add_synonym(word_list[1], word_list[2])
        elif word_list[0].lower() == 'delete':
            print("deleting a synonym...")
            # self.delete_synonym(word_list[1], word_list[2])
        elif word_list[0].lower() == 'feedback':
            print("giving feedback")
            # self.give_feedback(word_list)
        else:
            self.slack_client.api_call("chat.postMessage", channel=channel, 
                text="<show blaise poop> Not a valid command! ", as_user=True)            



    """
    Determine whether or not a message directed at bot 
    is a supported command. If not, show them picture 
    of @pascalrascal's poop
    """
    def validate_command(self, command_text, channel):
        ""


    """
    Support command to add a new synonym to root emoji. 
    """
    def add_synonym(self, new_synonym, root_word, channel):
        ""
        # self.check_root_word(new_synonym)
        


    """ 
    Support command to delete synonym of root emoji. 
    """
    def delete_synonym(self, new_synonym, root_word, channel):
        ""
    # make sure synonym is not a root 


    """
    Send @gatesyp a DM containing feedback. 
    How to do this on different servers? 
    """
    def give_feedback(self, command_text, channel): 
        ""

    def check_root_word(synonym):
        if self.emoji_map[word] == word:
            return True
        return False

    def send_message(text, channel): 
        ""
