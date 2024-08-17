import feedparser

FEED_URL = "https://medium.com/feed/@roekhan.dani.maulana"

def fetch_medium_posts(feed_url, num_posts=10):
    feed = feedparser.parse(feed_url)
    posts = []

    for entry in feed.entries[:num_posts]:
        title = entry.title
        link = entry.link
        image_url = entry.media_thumbnail[0]['url'] if 'media_thumbnail' in entry else None
        posts.append((title, link, image_url))

    return posts

def update_readme(posts):
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

    # Prepare new content
    new_content = ""
    for title, link, image_url in posts:
        new_content += f"- [{title}]({link})\n"
        if image_url:
            new_content += f"  ![Post Image]({image_url})\n"
        new_content += "\n"

    # If markers are found, replace the content in between
    if start_idx is not None and end_idx is not None:
        updated_content = readme_content[:start_idx + 1] + [new_content] + readme_content[end_idx:]
    else:
        # If markers are not found, append the new content at the end
        updated_content = readme_content + [f"\n{start_marker}\n"] + [new_content] + [f"\n{end_marker}\n"]

    # Write the updated content back to README.md
    with open('README.md', 'w') as f:
        f.writelines(updated_content)

if __name__ == "__main__":
    posts = fetch_medium_posts(FEED_URL)
    update_readme(posts)
