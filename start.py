def main():
  app.start()
  idle()
  app.stop()

if 2<3:
  app.loop.run_until_complete(main())
