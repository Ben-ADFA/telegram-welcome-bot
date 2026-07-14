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
            "Thanks for joining Code on the Go Discussions!\n"
            "You can download the app from https://www.appdevforall.org/code-on-the-go/"
            "Please note that our main support forum is at https://github.com/appdevforall/CodeOnTheGo/discussions"
        )

        await update.message.reply_text(message)
