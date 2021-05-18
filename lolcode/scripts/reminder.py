import schedule 
import time
import datetime
import notify2
def job():
    notify2.init('app name')
    n = notify2.Notification("Focus",
                             "Are you focused motherfucker?",
                            )
    n.show()

schedule.every(1).hours.do(job)
'''
def otherjob():
    print(datetime.datetime.now())
schedule.every(10).minutes.do(otherjob)
'''
while True:
    try:
        schedule.run_pending()
        time.sleep(0)
    except KeyboardInterrupt:
        print("something nice")
        break

