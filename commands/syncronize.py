from crontab import CronTab
import os
from adapter.drive import Drive
import getpass,platform



class Syncronize:
    COMMENT = "CloudBackup Syncronize Action, must be kept"
    
    def setup(self):
        cron = CronTab(user=True)
        script = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..','cloud_backup.py'))
        job = next(cron.find_comment(self.COMMENT), None)
        if job:
            pass
        else:
            job = cron.new(command="python {} syncronize".format(script), comment=self.COMMENT)
            job.every().day()
            cron.write()

    def run(self):
        backup_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..','Backups'))
        drive = Drive()

        for filename in os.listdir(backup_dir):
            if not filename.startswith("."):
                full_path = os.path.join(backup_dir, filename)
                drive.send_file(full_path, "{}_{}".format(getpass.getuser(),platform.node()))
