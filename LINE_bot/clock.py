from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request
import datetime

sched = BlockingScheduler()

@sched.scheduled_job('cron', minute = '*/20')
#@sched.scheduled_job('cron', day_of_week='mon-fri', minute = '*/2')
def scheduled_job():
    print('=====APScheduler CRON=========')
    print('This job runs every day */20 min')
    print(f"{datetime.datetime.now().ctime}")
    print('=====APScheduler CRON=========')
    
    url = 'https://med-tester.herokuapp.com/'
    conn = urllib.request.urlopen(url)
    
    for key, value in conn.getheaders():
        print(key, value)

sched.start()