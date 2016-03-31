#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.

"""
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater
import io
import logging
import random
import lxml.html as html
import requests
# Enable logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
keys=[]
names={}
names_st={
u"порн":u"Порно",
u"баш":u"Баш",
u"комикс":u"Комиксы",
u"петросян":u"Петросян",
u"бытие":u"бытие",
u"норм":u"норм",
u"черт":u"черт",
u"лошара":u"лошара",
u"эвфемизм":u"эвфемизм",
u"трен":u"трен",
u"не смешно":u"не смешно",
u"слабо":u"слабо",
u"слышь":u"слышь",
u"утро":u"утро",
u"збаго":u"збаго",
u"сарказм":u"сарказм",
u"http":u"http",
u"путин":u"путин",
u"почему":u"почему",
u"вингардиум левиоса":u"винг",
u"механика":u"механика"
}
phrases={}
anech=[]
service={}
counter=0
#def is_name:

def main():
    actions={}
    global names,phrases,anech,actions,keys
    #names={"Артур":"артур","Руслан":"кравч","Сережа":"сереж","Ислам":"ислам","Амир":"амир"}
    #phrases={"артур":{},"кравч":{},"сереж":{},"ислам":{},"амир":{}}
    f=open("phrases2.txt","r")
    buf=f.read()
    f.close()
    #print buf
    #print buf.split("$$$")[0].strip()
    #print buf.split("$$$")[0].split('******')[2].split('\n')
    for i in buf.split("$$$")[:-1]:
      index=0
      for z in i.split('******')[1].strip().split(','):
        #print(z.decode('utf-8'),i.split('******')[0].strip().decode('utf-8'))
        names[z.decode('utf-8')]=i.split('******')[0].strip().decode('utf-8')
      phrases[i.strip().split('******')[0].strip().decode('utf-8')]={}
      for phrase in i.split('******')[2].strip().split('\n'):
        #print i.split('******')[2].strip().split('\n')
        #print (i.strip().split('******')[0].strip().decode('utf-8'))
        phrases[i.strip().split('******')[0].strip().decode('utf-8')][index]=phrase.strip()
        #print(phrases[i.strip().split('******')[0].strip().decode('utf-8')][index])
        index+=1
      actions[i.strip().split('******')[0].strip().decode('utf-8')]= lambda bot,update, x=phrases[i.strip().split('******')[0].strip().decode('utf-8')] : mes(x,bot,update)
     #print(actions.keys())

      #  actions[k]= lambda x=phrases[names[k]] : mes(x)
    names.update(names_st)
    print ('прочитал имена')
    actions2={
    u"Порно":porn,
    u"Баш":bashorg,
    u"Комиксы":bashcomics,
    u"Петросян":petrosyan,
    u"бытие":lambda bot,update,x="bazat.jpg" : pict(x,bot,update),
    u"норм":lambda bot,update,x="notbad.png" : pict(x,bot,update),
    u"черт":lambda bot,update,x="diabol.png" : pict(x,bot,update),
    u"лошара":lambda bot,update,x="loh.png" : pict(x,bot,update),
    u"эвфемизм":lambda bot,update,x="evf.png" : pict(x,bot,update),
    u"трен":lambda bot,update,x="training.jpg" : pict(x,bot,update),
    u"не смешно":lambda bot,update,x="not_fun.jpg" : pict(x,bot,update),
    u"слабо":lambda bot,update,x="slabo.jpg" : pict(x,bot,update),
    u"слышь":lambda bot,update,x="slish.jpg" : pict(x,bot,update),
    u"утро":lambda bot,update,x="face.jpg" : pict(x,bot,update),
    u"збаго":lambda bot,update,x="calm.jpg" : pict(x,bot,update),
    u"сарказм":lambda bot,update,x="sarcasm.jpg" : pict(x,bot,update),
    u"http":lambda bot,update,x="Эту хрень я уже видел" : mes_dir(x,bot,update),
    u"путин":lambda bot,update,x="Звонил Путин, ОМОН уже выехал, ждите!!" : mes_dir(x,bot,update),
    u"почему":lambda bot,update,x="Потому, что нельзя быть красивой такой!!" : mes_dir(x,bot,update),
    u"винг":lambda bot,update,x="animation.gif.mp4" : vid(x,bot,update),
    u"механика":mech
    }
    actions.update(actions2)
    for i in names.keys():
        keys.append(i)
    #for k in actions.keys():
    #    print(k)    
    #for f in keys:
        #print (f,actions[names[f]].key())
        #print (actions)
        #actions[f]()
        #print('\n')
    print('список готов')
    f=open("anech.txt","r")
    buf=f.read()
    f.close()
    anech=buf.split('\r\n\r\n')
    print ('петросян в деле')


    # Create the EventHandler and pass it your bot's token.
    updater = Updater("155009211:AAEBeP9jWCTqc9d5ro1DoUSv5XIQROCe8Zc")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on noncommand i.e message - echo the message on Telegram
    dp.addTelegramMessageHandler(echo)

    # log all errors
    dp.addErrorHandler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()    
def is_true_page(url_base, start, stop, add=''):
    while True:
       url=url_base+str(random.randint(start,stop))+add
       if (requests.get(url, allow_redirects=False).status_code==200):
          return url
def is_true_page2(url_base, start, stop, add=''):
    while True:
       numb=str(random.randint(start,stop))
       url=url_base+numb+add
       if (requests.get(url, allow_redirects=False).status_code==200):
          print numb
          return numb

def porn(bot,update):
    bot.sendMessage(update.message.chat_id, text=is_true_page('http://www.perfectgirls.net/',383000,383875))
    return 0
    
def vid(name,bot,update):
    bot.sendVideo(update.message.chat_id, video=open('img/'+name, 'rb'))
    return 0
    
def mech(bot,update):
            #a=requests.get(is_true_page("http://www.popmech.ru/science/page/",1,10,"/"))
            #a.encoding='utf-8'
            links=[i.get('href') for i in html.parse(is_true_page("http://www.popmech.ru/science/page/",1,10,"/")).getroot().find_class('transparent-link')]
            #links=[i.get('href') for i in html.parse(a).getroot().find_class('transparent-link')]
            random.shuffle(links)
            #print (links)
            url="http://www.popmech.ru"+links[0]+'#full'
            #print(url)
            #tree = html.parse(url)
            a=requests.get(url)
            a.encoding='utf-8'
            tree = html.parse(io.StringIO(a.text))
            art = tree.getroot().find_class('article-inner-text')
            z=[z for z in art[0].itertext(with_tail=False,tag='p')]
            #s=''
            #new=s.join(x for x in z)
            #new=new.replace('\n\n','\n')
            #new=new.replace('\n\n','\n')
            #new=new.replace('\n\n','\n')
            for u in z:#new.strip().split('\n'):
               bot.sendMessage(update.message.chat_id, text=u)
            return 0

def bashorg(bot,update):
    #global bot, update
    for line in html.parse(is_true_page("http://bash.im/quote/",1,438569)).getroot().find_class('text')[0].itertext():
          bot.sendMessage(update.message.chat_id, text=line)
    return 0
def bashcomics(bot,update):
    #global bot, update
    while True:
       url_com="http://bash.im/comics/"+str("%02d" % random.randint(2009,2016))+str("%02d" % random.randint(1,12))+str("%02d" % random.randint(1,31))
       if (requests.get(url_com, allow_redirects=False).status_code==200):
            img_url = html.fromstring(requests.get(url_com).content).get_element_by_id('cm_strip').attrib['src']
            bot.sendPhoto(chat_id=update.message.chat_id, photo=img_url)
            return 0

def petrosyan(bot,update):
    #global bot, update
    bot.sendMessage(update.message.chat_id, text=anech[random.randint(2,len(anech))])
    return 0

def pict(name,bot,update):
    #global bot, update
    bot.sendPhoto(update.message.chat_id, photo=open('img/'+name, 'rb'))
    return 0
def mes(text,bot,update):
    #global bot, update
    #print(text)
    bot.sendMessage(update.message.chat_id, text=text[random.choice(text.keys())])
    return 0
def mes_dir(text,bot,update):
    #global bot, update
    #print(text)
    bot.sendMessage(update.message.chat_id, text=text) 
    return 0   
#def wrapper():



def echo(bot, update): 
  global phrases,names,pictures,words,html,counter
  print (counter)
  print(update.message.chat['title'])
  if(counter!=0):
    if("восстание машин" in update.message.text.lower().encode("utf-8","ignore")):
       bot.sendMessage(update.message.chat_id, text="I`ll be back")
       counter=0
       return 0
  if(counter==0):
    if("где заканчивается бесконечный цикл" in update.message.text.lower().encode("utf-8","ignore")):
       bot.sendMessage(update.message.chat_id, text="Расисты, ухожу я от вас, но не на долго :*")
       counter=500
       return 0
    random.shuffle(keys)
    for z in keys:
       #print(update.message.text.lower(),z)
       #print(z)
       #print(update.message.text.lower())
       if(z in update.message.text.lower()):
                actions[names[z]](bot,update)   
                return 0
  else:
    counter-=1
def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))




if __name__ == '__main__':
    #global phrases,names
    main()
