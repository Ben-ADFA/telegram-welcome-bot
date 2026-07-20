import logging
from datetime import time
from zoneinfo import ZoneInfo

from telegram.ext import (
    Application,
    ContextTypes
)

from config import BOT_TOKEN, CHAT_ID


logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


async def daily_welcome(context: ContextTypes.DEFAULT_TYPE):
    message = (
        "👋 Welcome to the Code on the Go community!\n\n"
        "Feel free to ask questions, share projects, "
        "and help other members.\n\n"
        "Have a great day!"
    )

    await context.bot.send_message(
        chat_id=CHAT_ID,
        text=message
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    pacific = ZoneInfo("America/Los_Angeles")

    app.job_queue.run_daily(
        daily_welcome,
        time=time(hour=7, minute=0, tzinfo=pacific)
    )

    print("Community Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()