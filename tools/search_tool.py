import requests
from dotenv import dotenv_values


def search_tool(input_list):
    """
    Search the given query on google.

    Parameters:
    input_list (list): A list containing only the query to search on google.

        Example format: ["longest river in the world"]

    Returns:
    (str): The formatted result of the search or an error message if something goes wrong.
    """
    try:
        query = input_list[0]
        CONFIG = dotenv_values("./config/.env")
        API_KEY = CONFIG["SERPER_API_KEY"]
        params = {
            'q': query,
            'api_key': API_KEY
        }
        response = requests.get(
            "https://google.serper.dev/search", params=params)
        data = response.json()
        formatted_output = ""
        for result in data["organic"]:
            formatted_output = formatted_output + result["snippet"] + "\n"
        return formatted_output

    except Exception as e:
        return "\nError ocurred." + e
