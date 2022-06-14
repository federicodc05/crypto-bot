import cryptocompare as cc
import telegram
import datetime as dt
import matplotlib.pyplot as plt

def color(hval):
    if hval[len(hval)-1]['high'] >= hval[len(hval)-2]['high']:
        return "lime"
    else:
        return "red"

#/conv <coin> [amount]
def crypto_handler(update,context):
    if len(context.args) == 0:
        update.message.reply_text(text="Insert a valid argument", parse_mode=telegram.ParseMode.HTML)
        return
    num = 1 if len(context.args) == 1 else int(context.args[1])
    coin = str(context.args[0]).upper()
    value = cc.get_price(coin, currency='USD')
    print(value)
    resp = "Invalid coin" if value is None else f"{num} {coin} = <b>{value[coin]['USD'] * num}</b> <i>USD</i>"
    update.message.reply_text(text=resp,parse_mode=telegram.ParseMode.HTML)


#/graph <coin>
def graph_handler(update,context):
    if len(context.args) == 0:
        update.message.reply_text(text="Insert a time and a date", parse_mode=telegram.ParseMode.HTML)
        return
    coin = str(context.args[0]).upper()
    date = dt.datetime.today()
    date = date.replace(hour=0,minute=0,second=0,microsecond=0)
    value = cc.get_historical_price_day(coin, 'USD', limit = 365, toTs = date)
    fig, ax = plt.subplots()
    x = [dt.datetime.fromtimestamp(m['time']) for m in value]
    y = [m['high'] for m in value]
    ax.plot(x, y, color=color(value))
    ax.set_facecolor((24 / 255, 37 / 255, 51 / 255))
    ax.set_xlabel('Date')
    ax.set_ylabel('Price (USD)')
    plt.suptitle(f"{coin} price as of {date}")
    plt.xticks([])
    fig.savefig("plot.png")
    #plt.plot()
    with open("plot.png", 'rb') as photo:
        graph = photo.read()
        update.message.reply_photo(photo=graph)


#error handler
def error_handler(update,context):
    print(f"Update {update} caused error {context.error}")
