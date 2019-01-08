from __future__ import print_function
from crontab import CronTab
import sys
import os
from commands.syncronize import Syncronize

class CreateBackup:
    def run_setup(self):
        cron = CronTab(user=True)
        dest = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..','Backups/'))
        if len(sys.argv) == 3:
            source = sys.argv[2]
        else:
            source = raw_input("Source Directory to backup: ")

        job = cron.new(command="tar zcvf '{}' '{}'".format(os.path.join(dest, source.split(os.path.sep)[-1]+".tar.gz"), source))
        job.every().day()
        print(job)
        cron.write()
        Syncronize().setup()

        
        
