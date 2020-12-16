from apscheduler.schedulers.blocking import BlockingScheduler
import jsoncheack
sched = BlockingScheduler()
@sched.scheduled_job('interval' ,minutes=1)
def timed_job():
    jsoncheack.main()

if __name__ == "__main__":
    sched.start()