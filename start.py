from pyrogram.handlers import MessageHandler, CallbackQueryHandler, EditedMessageHandler

def start(client,message):
  message.reply_text("Hello Welcome How are You✨")
  


async def main():
  await app.start()
  logging.info("bot started")
  await idle()
  await app.stop()

if 2<3:
  app.loop.run_until_complete(main())
