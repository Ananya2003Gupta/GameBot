import os
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
import commands as com

# Put your telegram bot token as an environment variable named KEY
key = os.environ['KEY']
print("Bot has Started....")


def introduce(name):
    print(f'Hi {name}')


def start_command(update, context):
    update.message.reply_text(
        "Type '/game' to start playing the games :). Use '/help' to list the commands"
    )


def help_command(update, context):
    update.message.reply_text("""Help menu:
  /start : To start the bot
  /help  : To get help regarding the commands for the bot
  hey,hello,hi or sup  : Salutations to say hi to bot
  /game  : To start the game
  """)

def game_command(update, context):
  com.item = 0
  update.message.reply_text("""You can only play the game once!
To restart the game or play a new game
Type your response:
    rock paper scissors
    hangman 
    guess the number
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

    dp.add_handler(CommandHandler("game", game_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
