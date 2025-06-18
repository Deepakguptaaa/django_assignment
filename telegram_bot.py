import os
import django
from telegram.ext import Updater, CommandHandler
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from myapp.models import TelegramUser  # Adjust if your model is in another app

# Replace with your real bot token
BOT_TOKEN = '7097214803:AAFjpoiyzxHvccqq8KZJJa-lGtriy8y53ek'

def start(update, context):
    username = update.message.from_user.username
    print(f"Received /start from: {username}")
    TelegramUser.objects.get_or_create(username=username)
    update.message.reply_text(f"Hello {username}, you have been registered!")

def main():
    print("Starting bot...")
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    print("Bot is polling...")  # This should always show
    updater.idle()

if __name__ == '__main__':
    main()

