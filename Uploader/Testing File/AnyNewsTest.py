import feedparser

url = "https://rss-bridge.org/bridge01/?action=display&bridge=YoutubeBridge&context=By+playlist+Id&p=PLn9UjXML6HFXsug_7o0uvtqjZ-_fRyfBO&duration_min=&duration_max=&format=Mrss"
feed = feedparser.parse(url)

print("Feed Title:", feed.feed.title)
print("Feed Description:", feed.feed.description)
print("Feed Link:", feed.feed.link)

for entry in feed.entries:
    print("Entry Title:", entry.title)
    print("Entry Link:", entry.link)
    print("Entry Published Date:", entry.published)
    print("Entry Summary:", entry.summary)
    print("\n")