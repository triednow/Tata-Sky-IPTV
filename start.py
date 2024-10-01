async def main():
  await app.start()
  await idle()
  await app.stop()

if 2<3:
  app.loop.run_until_complete(main())
