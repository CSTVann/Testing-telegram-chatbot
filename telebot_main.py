import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from typing import Final

# Bot Token and Username
Token: Final = "8194868944:AAEERu71UzPPEjvh4pBHA3zrmDTn7F9_haM"
BOT_USERNAME: Final = "@careptestingbot"

class CarepBot:
    def __init__(self):
        self.app = Application.builder().token(Token).build()
        self.setup_handlers()

    def setup_handlers(self):
        self.app.add_handler(CommandHandler('start', self.start_command))

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text("Hello! I'm your bot, and I am ready to help!")

    def run(self):
        print('Starting bot...')
        self.app.run_polling(poll_interval=5)

if __name__ == '__main__':
    bot = CarepBot()
    bot.run()
