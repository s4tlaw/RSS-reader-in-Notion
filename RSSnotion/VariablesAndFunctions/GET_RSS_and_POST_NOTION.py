import feedparser
import requests
from VariablesAndFunctions.Date_related_function import *
from VariablesAndFunctions.previous_excecute_time_store import *
from envANDsub import *

previous_excecute_time_dtformat = datetime.strptime(previous_excecute_time, "%a, %d %b %Y %H:%M:%S %z")

def get_rss_from_web(follow_channels, dbID):
    for url in follow_channels:
        fetch_rss_data(url, dbID)

    return "Done"

def fetch_rss_data(url, dbID):
    feed = feedparser.parse(url)
    for entry in feed.entries:
        entry_published_dtformat = datetime.strptime(check_published_format(entry.published), "%a, %d %b %Y %H:%M:%S %z")
        if previous_excecute_time_dtformat <= entry_published_dtformat :

            title = entry.title
            link = entry.link

            properties_data = {
                "Topic": {
                    "id": "title",
                    "type": "title",
                    "title": [{
                        "text": {
                            "content": title}}]},
                "URL": {
                    "url": link},
                "Sources": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": feed.feed.title}}]},
                "Date": {
                    "date": {
                        "start": entry_published_dtformat.isoformat()
                    }
                }
            }


            create_page(NOTION_TOKEN, dbID, properties_data)

            # print("Entry Title:", entry.title)
            # print("Entry Link:", entry.link)
            # print("Entry Published Date:", entry.published)
            # print("Entry Summary:", entry.summary)
            # print("\n")


def create_page(NOTION_TOKEN, input_data2 , input_data3: dict):

    api_url = "https://api.notion.com/v1/pages"

    headers = {
        "Authorization": "Bearer " + NOTION_TOKEN,
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    }

    json_file = {
        "parent": {"database_id": input_data2},
        "properties": input_data3,
    }

    res = requests.post(api_url, headers=headers, json=json_file)
    # print(res.status_code)
    return res

