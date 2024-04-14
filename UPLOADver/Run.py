from datetime import datetime
from VariablesAndFunctions.GET_RSS import get_rss_from_web
from VariablesAndFunctions.GET_RSS2 import get_rss_from_web2
from rss_feed_subscribe import *


def update_previous_excecute_time():
    file = open("VariablesAndFunctions/previous_excecute_time_store.py", "w+")
    now = datetime.now()
    last = now.strftime("%a, %d %b %Y %H:%M:%S %z")
    file.write("previous_excecute_time = " + '"' + last + "+0800" + '"')
    file.close()


get_rss_from_web2(rss_feed_subscribe_HK)
get_rss_from_web(rss_feed_subscribe_WORLD)
update_previous_excecute_time()
