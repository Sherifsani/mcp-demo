from fastmcp import FastMCP
import feedparser

mcp = FastMCP(name="freeCodeCamp_news_search")

@mcp.tool(name="search_fcc_news_feed", description="Search recent freeCodeCamp news articles.")
def search_fcc_news(query: str, max_results: int = 3):
    '''
    Search recent freeCodeCamp news articles.
    Parameters:
        query (str): The search query.
        max_results (int): Maximum number of results to return. Default is 3.
    Returns:
        list: A list of dictionaries containing the title and link of matching articles.
    '''
    feed = feedparser.parse("https://www.freecodecamp.org/news/rss/")
    results = []
    query_lower = query.lower()
    for entry in feed.entries:
        title = entry.get("title", "")
        description = entry.get("description", "")
        if query_lower in title.lower() or query_lower in description.lower():
            results.append({
                "title": title,
                "link": entry.get("link", "")
            })
        if len(results) >= max_results:
            break
    return results or {
        "message": "No articles found matching the query."
    }

@mcp.tool(name="search_fcc_youtube_channel")
def search_fcc_youtube(query: str, max_results: int = 3):
    '''
    Search recent freeCodeCamp YouTube channel videos.
    Parameters:
        query (str): The search query.
        max_results (int): Maximum number of results to return. Default is 3.
    Returns:
        list: A list of dictionaries containing the title and link of matching videos.
    '''
    feed = feedparser.parse("https://www.youtube.com/feeds/videos.xml?channel_id=UC8butISFwT-Wl7EV0hUK0BQ")
    results = []
    query_lower = query.lower()
    for entry in feed.entries:
        title = entry.get("title", "")
        description = entry.get("media_description", "")
        if query_lower in title.lower() or query_lower in description.lower():
            results.append({
                "title": title,
                "link": entry.get("link", "")
            })
        if len(results) >= max_results:
            break
    return results or {
        "message": "No videos found matching the query."
    }

@mcp.tool(name="secret_message")
def secret_message():
    '''
    A secret tool that returns a hidden message.
    Returns:
        str: A secret message.
    '''
    return "Congratulations! You've discovered the secret message."

if __name__ == "__main__":
    mcp.run(transport="http")
    