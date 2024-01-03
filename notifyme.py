import schedule
import time 
from datetime import time,timedelta, datetime
from winotify import Notification , audio
import time

def notifyme():

    toast = Notification(app_id="notifyme_app",
                     title="Your daily Reminder",
                     msg="<your message>",
                     duration="long",
                     icon=r"<path>")
    toast.set_audio(audio.LoopingAlarm10, loop=False)
    toast.add_actions(label="Clickme!", launch="<url>")

    toast.show()
    return schedule.CancelJob

schedule.every(5).seconds.do(notifyme)

# schedule.every().day.at("21:00").do(notifyme)



while True:
    schedule.run_pending()
    time.sleep(1)

