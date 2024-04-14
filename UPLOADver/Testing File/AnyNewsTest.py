import feedparser

url = "https://www.scmp.com/rss/3/feed"
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