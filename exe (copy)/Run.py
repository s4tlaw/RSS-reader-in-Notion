from datetime import datetime, timezone
from VariablesAndFunctions.GET_RSS import get_rss_from_web
from VariablesAndFunctions.GET_RSS_FORDUMBWEBSITE import get_rss_from_web_dumb
from environment import *
from rss_feed_subscribe import *


def update_previous_excecute_time(wt):
    file = open("VariablesAndFunctions/previous_excecute_time_store.py", "w+")
    file.write("previous_excecute_time = " + '"' + wt +'"')
    file.close()


upt = datetime.now(timezone.utc)
upt = datetime.strftime(upt, "%a, %d %b %Y %H:%M:%S %z")


get_rss_from_web(rss_feed_subscribe_WORLD, DATABASE_ID_WD)
get_rss_from_web(DATABASE_ID_YT, rss_feed_subscribe_YT)
get_rss_from_web_dumb(rss_feed_subscribe_HK_dumb, DATABASE_ID_HK)
get_rss_from_web_dumb(rss_feed_subscribe_WORLD_dumb, DATABASE_ID_WD)


update_previous_excecute_time(upt)
