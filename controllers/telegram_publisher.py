import requests
from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = '@justicIA_arg'

def send_telegram_message(message):
  text = format_text(message)
  print(f"Telegram text: {text}")
  url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
  payload = {
    "chat_id": CHAT_ID,
    "text": message,
    "parse_mode": "Markdown"
  }
  response = requests.post(url, json=payload)
  return response.json()

def format_text(text):
  escape_chars = r'\_*[]()~`>#+-=|{}.!'
  escaped_text = ''.join(['\\' + char if char in escape_chars else char for char in text])
  return escaped_text.replace('\n', '\\n')

def post_to_telegram(text):
  token = TELEGRAM_TOKEN
  CHAT_ID = 'YOUR_CHAT_ID'
  BASE_URL = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={CHAT_ID}&text={text}"
  requests.get(BASE_URL)

def post_to_twitter(text):
  # Use Twitter API client like Tweepy or directly make requests to Twitter's API
  pass