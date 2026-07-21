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
            "Thanks for visiting Code on the Go Discussions!\n\n"
            "To any new users, feel free to introduce yourself and tell us why you're using Code on the Go.\n\n"
            "If you haven't done so, you can download the app here:\n"
            "https://www.appdevforall.org/code-on-the-go/\n\n"
            "If you need help, please note that our main support forum is here:\n"
            "https://github.com/appdevforall/CodeOnTheGo/discussions\n\n"
            "We look forward to hearing from you!\n\n"
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
        time=time(hour=9, minute=30, tzinfo=pacific)
    )

    print("Community Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()