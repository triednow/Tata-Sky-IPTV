from pyrogram.handlers import MessageHandler, CallbackQueryHandler, EditedMessageHandler
from code_samples.bt import ButtonMaker
async def start(client,message):
  await message.reply_text("Hello Welcome How are You✨ This Is A Tataplay Access Token Generator Made By @aryanchy451")
  buttons = ButtonMaker()
  buttons.ibutton("LOGIN WITH PASSWORD",'PASS')
  buttons.ibutton("LOGIN WITH OTP", 'OTP')
  reply_markup = buttons.build_menu(2)
  msg = "Select How To Login To Tataplay"
  return await sendMessage(message, msg, reply_markup)

def password (_, query):
  
async def main():
  await app.start()
  logging.info("bot started")
  app.add_handler(MessageHandler(start, filters=command('start')))
  await idle()
  await app.stop()

if 2<3:
  app.loop.run_until_complete(main())
