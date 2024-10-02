from pyrogram.handlers import MessageHandler, CallbackQueryHandler, EditedMessageHandler
from code_samples import bt
def start(client,message):
  message.reply_text("Hello Welcome How are You✨ This Is A Tataplay Access Token Generator Made By @aryanchy451")
  


async def main():
  await app.start()
  logging.info("bot started")
  app.add_handler(MessageHandler(start, filters=command('start')))
  await idle()
  await app.stop()

if 2<3:
  app.loop.run_until_complete(main())
