import feedparser

def fetch_latest_posts(feed_url, num_posts=10):
    feed = feedparser.parse(feed_url)
    posts = []
    for entry in feed.entries[:num_posts]:
        posts.append(f"- [{entry.title}]({entry.link})")
    return posts

if __name__ == "__main__":
    feed_url = 'https://medium.com/feed/@roekhan.dani.maulana'
    posts = fetch_latest_posts(feed_url)
    with open('latest_posts.md', 'w') as f:
        f.write("# Latest Medium Posts\n\n" + "\n".join(posts))
