from flask import Flask, request, abort
from datetime import date
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, ImagemapSendMessage)
from linebot.models import *
import requests, json
import OPDAid4_SN
from bs4 import BeautifulSoup
import requests
import re
import myBubbles

app=Flask(__name__)
#run_with_ngrok(app)

line_bot_api=LineBotApi(OPDAid4_SN.myLineBotApi)
handler=WebhookHandler(OPDAid4_SN.myWebhookHandler)
myID=OPDAid4_SN.myUserID
line_bot_api.push_message(myID,FlexSendMessage(alt_text='你好',contents=myBubbles.myBubble_greeting()))
@app.route('/')
def index():
  return '歡迎使用三總北投門診助手4.0!'


@app.route('/callback',methods=['POST'])
def callback():
  signature=request.headers['X-Line-Signature']
  body=request.get_data(as_text=True)
  try:
    handler.handle(body,signature)
  except InvalidSignatureError:
    abort(400)
  return 'OK'

@handler.add(MessageEvent,message=TextMessage)
def handle_message(event):
  message=text=event.message.text
  if re.match('門診時間',message):
    line_bot_api.reply_message(event.reply_token, FlexSendMessage(alt_text=message,contents=myBubbles.myBubble_OPDs(message)))
  elif re.match('醫師查詢',message):
    line_bot_api.reply_message(event.reply_token, FlexSendMessage(alt_text=message,contents=myBubbles.myBubble_doctors(message)))
  elif re.match('重大公告',message):
    line_bot_api.reply_message(event.reply_token, FlexSendMessage(alt_text=message,contents=myBubbles.myBubble_News(message)))
  elif re.match('費用申請',message):
    line_bot_api.reply_message(event.reply_token, FlexSendMessage(alt_text=message,contents=myBubbles.myBubble_Fee('123')))
  else:
    line_bot_api.push_message(myID,FlexSendMessage(alt_text='你好',contents=myBubbles.myBubble_greeting()))

if __name__=='__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)