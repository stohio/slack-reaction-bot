import json

class Emoji:
    # initialize the class instance
    def __init__(self, slack_client):
        # grabs the custom emoji list for server
        self.custom_emoji_list = slack_client.api_call("emoji.list")["emoji"] 
        # load emojis file
        with open('emoji.json') as data_file:
            self.data = json.load(data_file)

    def search_list(self, query_list):
        result_set = list()
        for query in query_list:
            if query in self.custom_emoji_list:
                result_set.append(query)
            result_set.append(self.find_query(query))
        return result_set

    def format_text(self, message):
        formatted_message = message.lower()
        return formatted_message

    def find_query(self, query):
        for sub_list in self.data:
            if query == sub_list["short_name"]:
                return query

