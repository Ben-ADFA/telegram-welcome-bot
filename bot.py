from telegram.ext import (
    Application,
    MessageHandler,
    filters
)

from config import BOT_TOKEN
from handlers.welcome import welcome_new_member


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    welcome_handler = MessageHandler(
        filters.StatusUpdate.NEW_CHAT_MEMBERS,
        welcome_new_member
    )

    app.add_handler(welcome_handler)

    print("Community Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()