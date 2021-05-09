from content import main
import schedule
import time

schedule.every().day.at("23:50").do(main.main1())

while True:
  schedule.run_pending()
  time.sleep(1)