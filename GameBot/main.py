import os
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
import commands as com

key = os.environ['KEY']
print("Bot has Started....")


def introduce(name):
    print(f'Hi {name}')


def start_command(update, context):
    update.message.reply_text(
        "Type 'game' to start playing the games :). Use '/help' to list the commands"
    )


def help_command(update, context):
    update.message.reply_text("""Help menu:
  /start : To start the bot
  /help  : To Handle the bot
  hey,hello,hi or sup  : Salutations to say hi to bot
   game  : To start the game
  """)


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = com.responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(key, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))

    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
