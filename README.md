# Dust Star 🌟

A read-only web dashboard to visualize Reddit community trends.

## Overview

Dust Star is a **personal, non-commercial** web application that fetches publicly available Reddit post data and displays simple trend visualizations. It helps users discover trending and underappreciated discussions across specific subreddits.

## Features

- 📊 Visualize trending topics across selected subreddits
- 📈 Track post engagement metrics (upvotes, comment counts, posting times)
- 🔍 Discover underappreciated posts that deserve more attention
- 🖥️ Clean, responsive web dashboard built with Chart.js

## Important: What This App Does NOT Do

- ❌ Does NOT post, comment, vote, or send messages
- ❌ Does NOT collect, store, or share any user personal data
- ❌ Does NOT scrape or bulk-download Reddit data
- ❌ Does NOT train AI/ML models on Reddit content
- ❌ Does NOT use any write API endpoints
- ❌ Does NOT operate as an automated bot
- ❌ Is NOT commercial — zero monetization

## Technical Details

| Item | Detail |
|------|--------|
| Language | Python 3.10+ |
| Reddit Library | PRAW (Python Reddit API Wrapper) |
| Auth | OAuth2 — `read` scope only |
| Visualization | Chart.js / D3.js |
| Web Framework | Flask |
| Rate Limiting | Fully respects Reddit's limits (≤60 req/min) |
| Data Storage | None — all data is fetched in real-time, never stored |

## Target Subreddits

This app reads publicly available data from a small set of subreddits:

- r/technology
- r/science
- r/programming
- r/dataisbeautiful

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/stardustandone-ship-it/dust-star.git
   cd dust-star
2. Install dependencies:
   pip install -r requirements.txt
3. Configure Reddit API credentials:
   cp .env.example .env
   # Edit .env with your Reddit API credentials
4. Run the app:
  python app.py
