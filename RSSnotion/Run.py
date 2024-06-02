from datetime import datetime, timezone
from VariablesAndFunctions.GET_RSS_and_POST_NOTION import get_rss_from_web
from envANDsub import *

def update_previous_excecute_time(wt):
    file = open("/home/rekt/PycharmProjects/RSSnotion/VariablesAndFunctions/previous_excecute_time_store.py", "w+")
    file.write("previous_excecute_time = " + '"' + wt +'"')
    file.close()


upt = datetime.now(timezone.utc)
upt = datetime.strftime(upt, "%a, %d %b %Y %H:%M:%S %z")

get_rss_from_web(rss, DATABASE_ID_ALL)

update_previous_excecute_time(upt)
