import os
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from dotenv import load_dotenv

# Step 1: Load environment variables from the .env file
load_dotenv()

# Step 2: Get the Telegram bot token from the .env file
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Step 3: Initialize the bot application
application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

# Step 4: Function to handle the /start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to the J. Bunny Game! Tap to make J. Bunny kiss Boozy!")

# Step 5: Function to handle the /tap command
user_taps = {}

def tap(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if user_id not in user_taps:
        user_taps[user_id] = 0
    
    user_taps[user_id] += 1
    
    if user_taps[user_id] >= 10:
        update.message.reply_text("J. Bunny kisses Boozy! You’ve earned 10 J. Bunny tokens!")
        user_taps[user_id] = 0  # Reset taps after 10
    else:
        update.message.reply_text(f"Taps: {user_taps[user_id]}/10 - Keep tapping!")

# Step 6: Add handlers for the commands
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("tap", tap))

# Step 7: Start the bot
if name == "__main__":
    application.run_polling()
