import feedparser
import requests
from datetime import    datetime
from VariablesAndFunctions.Date_related_function import check_published_format
from VariablesAndFunctions.previous_excecute_time_store import previous_excecute_time

url = "https://feeds.bbci.co.uk/zhongwen/trad/rss.xml"


NOTION_TOKEN = "secret_J<yourtoken>L"
testdb = "0<yourdbid>0"
previous_excecute_time_dtformat = datetime.strptime(previous_excecute_time, "%a, %d %b %Y %H:%M:%S %z")

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,  # Bearer token
    "Content-Type": "application/json",  # Define content type you post to URL. See more on json content type
    "Notion-Version": "2022-06-28",  # Define version https://developers.notion.com/reference/versioning
}

def create_page(input_data1: dict, input_data2 , input_data3: dict):  # define "data" as dictionary
    # See more on Data Structures in python https://www.geeksforgeeks.org/python-data-structures/
    api_url = "https://api.notion.com/v1/pages"  # Define API URL of "creating a page"
    json_file = {  # Follow this to learn Notion Page Object Properties https://developers.notion.com/reference/page
        "parent": {"database_id": input_data2},
        "properties": input_data3,
    }
    res = requests.post(api_url, headers=input_data1, json=json_file)  # from request post
    # print(res.status_code)
    return res


def fetch_rss_data(url, dbID):
    feed = feedparser.parse(url)
    for entry in feed.entries:
        entry_published_dtformat = datetime.strptime(check_published_format(entry.published),
                                                     "%a, %d %b %Y %H:%M:%S %z")
        if previous_excecute_time_dtformat <= entry_published_dtformat:
            title = entry.title
            link = entry.link

            properties_data = {
                "News Title": {
                    "id": "title",
                    "type": "title",
                    "title": [{
                        "text": {
                            "content": title}}]},
                "Link": {
                    "url": link},
            }




            create_page(headers, dbID, properties_data)

            print("Entry Title:", entry.title)
            print("Entry Link:", entry.link)
            print("Entry Published Date:", entry.published)
            print("Entry Summary:", entry.summary)
            print("\n")


fetch_rss_data(url, testdb)

