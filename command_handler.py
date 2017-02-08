from slackclient import SlackClient

"""
Handle all commands
"""
class Command:
    def __init__(self, slack_client):
        ""
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
    def add_synonym(self, command_text, channel):
        ""
    # make sure synonym is not a root, and does not already exist
    # add the synonym


    """ 
    Support command to delete synonym of root emoji. 
    """
    def delete_synonym(self, command_text, channel):
        ""
    # make sure synonym is not a root 


    """
    Send @gatesyp a DM containing feedback. 
    How to do this on different servers? 
    """
    def give_feedback(self, command_text, channel): 
        ""

    def check_root_word(word):
        if self.emoji_map[word] == word:
            return True
        return False

    def send_message(text, channel): 
        ""
