from pyrogram.handlers import MessageHandler, CallbackQueryHandler, EditedMessageHandler
from code_samples.bt import ButtonMaker
import code_samples.login
async def start(client,message):
  await message.reply_text("Hello Welcome How are You✨ This Is A Tataplay Access Token Generator Made By @aryanchy451")
  buttons = ButtonMaker()
  buttons.ibutton("LOGIN WITH PASSWORD",'PASS')
  buttons.ibutton("LOGIN WITH OTP", 'OTP')
  reply_markup = buttons.build_menu(2)
  msg = "Select How To Login To Tataplay"
  return await sendMessage(message, msg, reply_markup)

def password(_, query):
  m = query.message
  get_id = app.ask(
        chat_id=m.chat.id,
        text="Enter Subscriber Id or /cancel to Stop Process"#API_TEXT.format(m.from_user.mention(style='md')),
    )
  api_id = get_id.text
  if is_cancel(query.message, api_id):
      return

  get_id.delete()
  get_id.request.delete()
  get_id = app.ask(
        chat_id=m.chat.id,
        text="Enter Phone Number Without +91 or /cancel to Stop Process"#API_TEXT.format(m.from_user.mention(style='md')),
    )
  phnum = get_id.text
  if is_cancel(query.message, phnum):
      return

  get_id.delete()
  get_id.request.delete()
  get_id = app.ask(
        chat_id=m.chat.id,
        text="Enter Password or /cancel to Stop Process"#API_TEXT.format(m.from_user.mention(style='md')),
    )
  passwd = get_id.text
  if is_cancel(query.message, passwd):
      return

  get_id.delete()
  get_id.request.delete()
  login.loginWithPass(sid=api_id, rmn=phnum, pwd=passwd)

def otp(_, query):
  m = query.message
  get_id = app.ask(
        chat_id=m.chat.id,
        text="Enter Subscriber Id or /cancel to Stop Process"#API_TEXT.format(m.from_user.mention(style='md')),
    )
  api_id = get_id.text
  if is_cancel(query.message, api_id):
      return

  get_id.delete()
  get_id.request.delete()
  get_id = app.ask(
        chat_id=m.chat.id,
        text="Enter Phone Number Without +91 or /cancel to Stop Process"#API_TEXT.format(m.from_user.mention(style='md')),
    )
  phnum = get_id.text
  if is_cancel(query.message, phnum):
      return

  get_id.delete()
  get_id.request.delete()
  login.generateOTP(sid=api_id, rmn=phnum)
async def main():
  await app.start()
  logging.info("bot started")
  app.add_handler(MessageHandler(start, filters=command('start')))
  await idle()
  await app.stop()

if 2<3:
  app.loop.run_until_complete(main())
