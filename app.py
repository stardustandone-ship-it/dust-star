"""
Dust Star - Reddit Community Trend Visualizer
A read-only, non-commercial web dashboard.
Uses Reddit OAuth2 API with 'read' scope only.
"""

import os
from flask import Flask, render_template, jsonify
import praw
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_reddit_client():
    """Initialize Reddit client with read-only OAuth2 access."""
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent="DustStar/1.0 (read-only trend visualizer by u/Capital-Rhubarb-2199)",
    )

@app.route("/")
def index():
    """Render the main dashboard page."""
    return render_template("index.html")

@app.route("/api/trends/<subreddit_name>")
def get_trends(subreddit_name):
    """Fetch top posts from a subreddit for trend visualization."""
    allowed_subreddits = ["technology", "science", "programming", "dataisbeautiful"]

    if subreddit_name not in allowed_subreddits:
        return jsonify({"error": "Subreddit not in allowed list"}), 403

    reddit = get_reddit_client()
    subreddit = reddit.subreddit(subreddit_name)

    posts = []
    for post in subreddit.hot(limit=25):
        posts.append({
            "title": post.title,
            "score": post.score,
            "num_comments": post.num_comments,
            "created_utc": post.created_utc,
            "url": post.url,
        })

    return jsonify({"subreddit": subreddit_name, "posts": posts})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
