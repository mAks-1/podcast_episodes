import feedparser
from fastapi import APIRouter, HTTPException

router = APIRouter()

RSS_URL = "https://feeds.npr.org/510289/podcast.xml"


@router.get("/rss")
async def get_rss_feed():
    try:
        feed = feedparser.parse(RSS_URL)
        episodes = [
            {"title": entry.title, "url": entry.link}
            for entry in feed.entries[:10]  # 10 last
        ]
        return episodes
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"RSS parsing error: {str(e)}")
