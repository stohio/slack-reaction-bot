import json

class Emoji:
    # initialize the class instance
    # grabs the custom emoji list for server
    def __init__(self, slack_client):
        self.custom_emoji_list = slack_client.api_call("emoji.list")["emoji"] 

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
        with open('emoji.json') as data_file:
            data = json.load(data_file)
        for sub_list in data:
            if query == sub_list["short_name"]:
                return query

