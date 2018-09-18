from telegram.ext import Updater, CommandHandler
from engine import get_random_quote

# Your bot token (from BotFather)
token = "657281898:AAH8Mu6GCJTBGX-dqV8yP2nJMbJErtY-bFA"

def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text=("Ossequi %s. Scrivi /quote ed otterrai una frase presa dalla vastità della rete cibernetica mondiale scelta casualmente "
														   %
														  update.message.from_user.name))

def quote(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id,
					text=get_random_quote())

def main():
	updater = Updater(token);
	dp = updater.dispatcher

	# Define all the commands that the bot will receive
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("quote", quote))

	# Start the bot
	updater.start_polling()
	print("================================")
	print("========= Bot Running ==========")
	print("================================")

	updater.idle()


if __name__ == "__main__":
	main()