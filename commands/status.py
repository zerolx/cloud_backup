from config import Config
from crontab import CronTab

class Status:
    def __init__(self):
        self.config = Config()
    
    def format(self):
        config = self.config.get_config()
        cron = CronTab(user=True)
        crontabjobs = '\n\t'.join([str(job) for job in cron])
        return """ CronTab Configuration:
        {}
        """.format(crontabjobs)
