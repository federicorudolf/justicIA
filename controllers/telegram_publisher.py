import requests
from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = '@justicIA_arg'

def send_telegram_message(message):
  url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
  payload = {
    "chat_id": CHAT_ID,
    "text": message,
    "parse_mode": "MarkdownV2"
  }
  response = requests.post(url, json=payload)
  return response.json()

def post_to_telegram(text):
  token = TELEGRAM_TOKEN
  CHAT_ID = 'YOUR_CHAT_ID'
  BASE_URL = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={CHAT_ID}&text={text}"
  requests.get(BASE_URL)

def post_to_twitter(text):
  # Use Twitter API client like Tweepy or directly make requests to Twitter's API
  pass