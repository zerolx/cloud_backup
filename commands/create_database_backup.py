from __future__ import print_function
from crontab import CronTab
import sys
import os
import getpass
from commands.syncronize import Syncronize

class CreateDatabaseBackup:
    def run_setup(self):
        dest = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..','Backups/'))
        if len(sys.argv) == 6:
            pname ,user, passwd, dbname = (sys.argv[2],sys.argv[3],sys.argv[4], sys.argv[5])
        else:
            pname = raw_input("Database Service name: ")
            user = raw_input("Database user: ")
            passwd = getpass.getpass("Database password: ")
            dbname = raw_input("Database name: ")

        pname = pname.lower().strip()
        if pname == "mysql":
            self.create_cron("mysqldump -u'{}' -p'{}' '{}' > '{}'".format(user, passwd, dbname, os.path.join(dest, dbname+".sql")))
        else:
            print("DATABASE {} NOT SUPPORTED YET!".format(pname))
        # "tar zcvf {} {}".format(os.path.join(dest, source.split(os.path.sep)[-1]+".tar.gz"), source)

    def create_cron(self,command):
        cron = CronTab(user=True)
        job = cron.new(command=command)
        # job.every().day()
        print(job)
        cron.write()
        Syncronize().setup()
