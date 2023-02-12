import requests
import json
import ast

class TCGHelper():

    def __init__(self, input):
        self.commands = {
            "!random":"https://www.tcghelper.com/v1/random",
            "!decklist":"https://www.tcghelper.com/v1/decklist",
            "!all":"https://www.tcghelper.com/v1/all"
        }
        self.users_command = str(input)


    def basic_commands(self):
        for command in self.commands:

            if command == "!all":
                return "Sorry, the all command doesn't work due to character limit"

            if self.users_command == command:
                command_response = requests.get(f"{self.commands[command]}")
                command_response = command_response.text
                command_response = command_response.replace("\\", "")
                command_response = command_response.replace("u00e9", "e")
                dictionary = ast.literal_eval(command_response)
                json_response = json.dumps(dictionary, indent=3, sort_keys=True)
                return json_response


        return "Sorry, this is not a valid command"

    def search_commmand(self):
        users_search = self.users_command.lower().split(" ")[1]
        search_response = requests.get(f"https://www.tcghelper.com/v1/search?query={users_search}")
        search_response = search_response.text
        search_response = search_response.replace("\\", "")
        search_response = search_response.replace("u00e9", "e")
        dictionary = ast.literal_eval(search_response)
        json_response = json.dumps(dictionary, indent=3, sort_keys=True)
        return json_response




