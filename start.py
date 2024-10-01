def main():
  app.start()
  app.idle()
  app.stop()

if 2<3:
  app.loop.run_until_complete(main())
