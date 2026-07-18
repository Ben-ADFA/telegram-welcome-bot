from telegram import Update
from telegram.ext import ContextTypes


async def welcome_new_member(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    if not update.message:
        return

    for member in update.message.new_chat_members:
        # Ignore bots joining
        if member.is_bot:
            continue

        name = member.first_name

        message = (
            f"👋 Welcome, {name}!\n\n"
            "Thanks for joining Code on the Go Discussions!\n\n"
            "Feel free to introduce yourself and tell us why you're using Code on the Go.\n\n"
            "If you haven't done so, you can download the app here:\n"
            "https://www.appdevforall.org/code-on-the-go/\n\n"
            "If you need help, please note that our main support forum is here:\n"
            "https://github.com/appdevforall/CodeOnTheGo/discussions\n\n"
            "We look forward to hearing from you!\n\n"
        )

        await update.message.reply_text(message)
