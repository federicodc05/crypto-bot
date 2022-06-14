from telegram.ext import *
import command_handlers as ch
# libraries to install: python-telegram-bot, cryptocompare, matplotlib

KEY = 'KEY_HERE' #Ask in private

#main
def main():
    updater = Updater(KEY, use_context=True)
    print("Ok")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("conv", ch.crypto_handler,pass_args=True))
    dp.add_handler(CommandHandler("graph", ch.graph_handler, pass_args=True))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
