from environment import *
import requests

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,  # Bearer token
    "Content-Type": "application/json",  # Define content type you post to URL. See more on json content type
    "Notion-Version": "2022-06-28",  # Define version https://developers.notion.com/reference/versioning
}

def create_page(input_data1: dict, input_data2 , input_data3: dict):  # def create_page(input_data1: dict, input_data2 , input_data3: dict, input_data4: dict):
    # See more on Data Structures in python https://www.geeksforgeeks.org/python-data-structures/

    api_url = "https://api.notion.com/v1/pages"  # Define API URL of "creating a page"

    json_file = {  # Follow this to learn Notion Page Object Properties https://developers.notion.com/reference/page
        "parent": {"database_id": input_data2},
        "properties": input_data3,
        #"children": [input_data4]

    }

    res = requests.post(api_url, headers=input_data1, json=json_file)  # from request post
    return res
