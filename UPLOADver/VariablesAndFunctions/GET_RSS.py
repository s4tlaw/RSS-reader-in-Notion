import feedparser
from VariablesAndFunctions.Date_related_function import *
from VariablesAndFunctions.previous_excecute_time_store import *
from VariablesAndFunctions.POST_Notion import *


previous_excecute_time_dtformat = datetime.strptime(previous_excecute_time, "%a, %d %b %Y %H:%M:%S %z")


def fetch_rss_data(url):
    feed = feedparser.parse(url)
    for entry in feed.entries:
        entry_published_dtformat = datetime.strptime(check_published_format(entry.published), "%a, %d %b %Y %H:%M:%S %z")
        if previous_excecute_time_dtformat <= entry_published_dtformat :

            title = entry.title
            link = entry.link
            # context = entry.summary

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
            # summary = {
            #     "object": "block",
            #     "type": "paragraph",
            #     "paragraph": {
            #         "rich_text": [{
            #             "type": "text",
            #                 "text": {
            #                 "content": context}}]}}

            create_page(headers, DATABASE_ID, properties_data)

            print("Entry Title:", entry.title)
            print("Entry Link:", entry.link)
            print("Entry Published Date:", entry.published)
            print("Entry Summary:", entry.summary)
            print("\n")


def get_rss_from_web(channels):
    for url in channels:
        fetch_rss_data(url)
    print("Done")


