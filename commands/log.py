from __future__ import print_function
from crontab import CronTab

class Log:
    def show(self):
        cron = CronTab(user=True)
        for d in cron.log: # Not working, probably bug in CronTab lib
            # pass
            print(str(d))
            print(str(d['pid']) + " - " + str(d['date']))
