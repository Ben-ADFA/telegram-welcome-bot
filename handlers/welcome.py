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
            "You can download Code on the Go here:\n"
            "https://www.appdevforall.org/code-on-the-go/\n\n"
            "Please note that our main support forum is at:\n"
            "https://github.com/appdevforall/CodeOnTheGo/discussions"
        )

        await update.message.reply_text(message)
