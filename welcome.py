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
            "Thanks for joining our community.\n"
            "Feel free to ask questions and participate!"
        )

        await update.message.reply_text(message)