import cryptocompare as cc
import telegram

#/conv <coin> [amount]
def crypto_handler(update,context):
    if len(context.args) == 0:
        update.message.reply_text(text="Insert a valid argument", parse_mode=telegram.ParseMode.HTML)
        return
    num = 1 if len(context.args) <= 1 else int(context.args[1])
    coin = str(context.args[0]).upper()
    value = cc.get_price(coin, currency='USD')
    print(value)
    resp = "Invalid coin" if value is None else f"{num} {coin} = <b>{value[coin]['USD']*num}</b> <i>USD</i>"
    update.message.reply_text(text=resp,parse_mode=telegram.ParseMode.HTML)

def error_handler(update,context):
    print(f"Update {update} caused error {context.error}")