from datetime import datetime
from VariablesAndFunctions.GET_RSS import get_rss_from_web
from environment import *
from rss_feed_subscribe import *


def update_previous_excecute_time():
    file = open("VariablesAndFunctions/previous_excecute_time_store.py", "w+")
    now = datetime.now()
    last = now.strftime("%a, %d %b %Y %H:%M:%S %z")
    file.write("previous_excecute_time = " + '"' + last + "+0800" + '"')
    file.close()


get_rss_from_web(rss_feed_subscribe_HK, DATABASE_ID_HK)
get_rss_from_web(rss_feed_subscribe_WORLD, DATABASE_ID_WD)
get_rss_from_web(DATABASE_ID_YT, rss_feed_subscribe_YT)

update_previous_excecute_time()
