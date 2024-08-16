import feedparser

def fetch_latest_posts(feed_url, num_posts=10):
    feed = feedparser.parse(feed_url)
    posts = []
    for entry in feed.entries[:num_posts]:
        posts.append(f"- [{entry.title}]({entry.link})")
    return posts

if __name__ == "__main__":
    feed_url = 'https://medium.com/feed/@yourusername'
    posts = fetch_latest_posts(feed_url)
    
    # Read the existing README content
    with open('README.md', 'r') as f:
        readme_content = f.readlines()

    # Find the section to update
    start_marker = "<!--START_SECTION:medium-->"
    end_marker = "<!--END_SECTION:medium-->"
    start_idx = None
    end_idx = None

    for idx, line in enumerate(readme_content):
        if start_marker in line:
            start_idx = idx
        if end_marker in line:
            end_idx = idx

    # If markers are found, replace the content in between
    if start_idx is not None and end_idx is not None:
        new_content = readme_content[:start_idx + 1] + ["\n".join(posts) + "\n"] + readme_content[end_idx:]
    else:
        # If markers are not found, append the new content at the end
        new_content = readme_content + [f"\n{start_marker}\n"] + posts + [f"\n{end_marker}\n"]

    # Write the updated content back to README.md
    with open('README.md', 'w') as f:
        f.writelines(new_content)
