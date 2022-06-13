from telegram.ext import *
import command_handlers as ch
# libraries to install: python-telegram-bot, cryptocompare

KEY = 'KEY_HERE' #Ask me in private :)

#main
def main():
    updater = Updater(KEY, use_context=True)
    print("Ok")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("conv", ch.crypto_handler,pass_args=True))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()