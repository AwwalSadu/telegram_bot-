import telegram.ext
import os
import pywhatkit
import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import pandas_datareader as web


token =  'Get your token from the Botfather on telegram' 


# Now we would write functions that we want our bot to do
def start(update, context):
    update.message.reply_text('Hi, My name is Martha.')
    update.message.reply_text('''I am here to assist you, The things i can do are:

Getting the /news for you

Get /weather update

Get Current /stock prices 

If you get confused use the /help command 
    
And soon i would be able to chat with you normally :)
    ''')


def help(update, context):
    update.message.reply_text("""The following commands are available: 
    /start -> Start bot 
    /help -> This message 
    /news -> Get news information 
    /contact -> contact developer 
    /stock -> Get stock prices: 
        To get stock price, 
        Use the /stock command with the ticker name of the company
        E.g (/stock APPL),This gives the current stock price of the company) 
    
     
    """)


def contact(update, context):
    update.message.reply_text('Message the developer at Saduawwal@gmail.com or +2347032942340')


def stock(update, context):
    ticker = context.args[0]
    data = web.DataReader(ticker, 'yahoo')
    price = data.iloc[-1]['Close']
    update.message.reply_text(f'The current price of {ticker} is ${price:.2f}')


#================================================= Getting news from Google news using beautiful soup ====================


def news(update, context):
    news_url = "https://news.google.com/news/rss" # Google news URL
    client = urlopen(news_url)  # OPenning the Url
    xml_page = client.read()    # Reading URL info
    client.close()

    soup_page = soup(xml_page, "xml")   # using beautiful soup to get the page info
    news_list = soup_page.findAll("item") # Getting info from the website (All items)
    # Print news title, url and publish date
    for i in range(10):
        for news in news_list:
            update.message.reply_text(news.title.text)  # News title
            update.message.reply_text(news.link.text)   # News link
            update.message.reply_text(news.pubDate.text)    # Date published
            update.message.reply_text('_' * 60)
            # print(news.title.text)
        # print(news.link.text)
        # print(news.pubDate.text)
        # print("-" * 60)

# ============================================= Weather function =========================================

def weather(update, context):
    update.message.reply_text("Hmmmmm, i am not sure of the current weather conditions soooooo :(")


def msg(update, context):
   update.message.reply_text(f'{update.message.text}')


# Our updater object 
updater = telegram.ext.Updater(token, use_context=True)

# our dispatcher
disp = updater.dispatcher

# Our command handler
disp.add_handler(telegram.ext.CommandHandler('start', start))
disp.add_handler(telegram.ext.CommandHandler('help', help))
disp.add_handler(telegram.ext.CommandHandler('contact', contact))
disp.add_handler(telegram.ext.CommandHandler('news', news))
disp.add_handler(telegram.ext.CommandHandler('stock', stock))
disp.add_handler(telegram.ext.CommandHandler('weather', weather))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, msg))

while True:
    updater.start_polling()
    updater.idle()


# This project was completed with the video aid of NeuralNine tutorial on youtube("Make sure to check him out ;)" )
