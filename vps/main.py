from flask import Flask,request,abort
from flask import request
import telebot
import bwg,netfront,cheap_nat,centerhop,iplc
'''
将之前的查流量脚本结合tg-bot开发，把查询工作交给服务器，实现多终端查询
采用pyTelegramBotAPI开源库，github自行搜索
采用flask框架
'''
token = 'your token'     #TG-bot的token
#url = 'https://example.com'     #webhook地址
path = '/path'     #访问路径，也可以在nginx中反代location处设置，自行选择
app = Flask(__name__)     #这里对应uwsgi中的callable，否则会找不到文件(手动滑稽)
bot = telebot.TeleBot(token,threaded=False)
###设置webhook，手动设置了，就移除掉了
'''bot.remove_webhook()
bot.set_webhook(url=url+path)'''

@app.route(path,methods=['POST']) #设置webhook入口
def webhook():
    if request.method == 'POST':
        update = telebot.types.Update.de_json(request.get_data().decode('utf-8'))
        bot.process_new_updates([update])
        return 'Ok',200
    else:
        abort(403)

#指令是自己设置的，鉴于我要分类查询，则直接用服务商代号设置为了指令集
@bot.message_handler()
def delmessage(message):
    text = message.text
    if text == '/bwg' :
        bot.send_message(message.chat.id, bwg.checkdata())
    elif text == '/netfront' :
        bot.send_message(message.chat.id, netfront.checkdata())
    elif text == '/cheapnat':
        bot.send_message(message.chat.id, cheap_nat.checkdata())
    elif text == '/centerhop':
        bot.send_message(message.chat.id, centerhop.checkdata())
    elif text == '/iplc':
        bot.send_message(message.chat.id, iplc.main())
    else:
        bot.send_message(message.chat.id, '你在淦神魔！')