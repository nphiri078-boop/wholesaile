#!/usr/bin/env python3
import os, requests, sys
msg = ' '.join(sys.argv[1:])
token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('TELEGRAM_CHAT_ID')
if token and chat_id:
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    requests.post(url, data={'chat_id': chat_id, 'text': msg})
    print("Telegram blast sent!")
else:
    print("Mock: Telegram blast: " + msg)
