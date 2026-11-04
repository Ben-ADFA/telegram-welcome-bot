import logging
from datetime import time
from zoneinfo import ZoneInfo
from telegram import LinkPreviewOptions
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
            "Thanks for visiting Code on the Go Official!\n\n"
            "Due to U.S. government sanctions, this is a one-way communication channel, "
            "meaning we do not reply to messages on Telegram. "
            "To read about the sanctions, please visit:\n"
            "https://appdevforall.org/updated-support-policy/\n\n"
            "If you haven't done so, you can download the app here:\n"
            "https://www.appdevforall.org/code-on-the-go/\n\n"
            "If you need help, please visit our main support forum:\n"
            "https://github.com/appdevforall/CodeOnTheGo/discussions\n\n"
            "Thanks for using the app!\n\n"
    )
    await context.bot.send_message(
        chat_id=CHAT_ID,
        text=message,
        link_preview_options=LinkPreviewOptions(is_disabled=True)
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()
    pacific = ZoneInfo("America/Los_Angeles")

    # Posts twice daily: 6:30 AM and 6:30 PM Pacific
    app.job_queue.run_daily(
        daily_welcome,
        time=time(hour=6, minute=30, tzinfo=pacific),
        name="welcome_morning"
    )
    app.job_queue.run_daily(
        daily_welcome,
        time=time(hour=18, minute=30, tzinfo=pacific),
        name="welcome_evening"
    )

    print("Community Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()