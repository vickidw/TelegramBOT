import requests
import feedparser
import time

BOT_TOKEN = "8678049736:AAFVArcwOGYwFq76G8GgLXKT1EcXo9zYeIU"
CHANNEL_USERNAME = "@tribestamil"
YOUTUBE_CHANNEL_ID = "UCe4Xx2aBYBTncbWnmw5mg6A"

RSS_URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={UCe4Xx2aBYBTncbWnmw5mg6A}"

last_video_id = None

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{8678049736:AAFVArcwOGYwFq76G8GgLXKT1EcXo9zYeIU}/sendMessage"
    data = {
        "chat_id": CHANNEL_USERNAME,
        "text": text,
        "parse_mode": "HTML"
    }
    requests.post(url, data=data)

while True:
    feed = feedparser.parse(RSS_URL)

    if feed.entries:
        latest = feed.entries[0]
        video_id = latest.yt_videoid
        title = latest.title
        link = latest.link

        if video_id != last_video_id:
            message = f"🎬 <b>{title}</b>\n\nWatch here:\n{link}"
            send_telegram_message(message)
            last_video_id = video_id

    time.sleep(600)
