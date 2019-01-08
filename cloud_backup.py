from __future__ import print_function
from adapter.drive import Drive
from commands.status import Status
from commands.log import Log
from commands.create_backup import CreateBackup
from commands.create_database_backup import CreateDatabaseBackup
from commands.syncronize import Syncronize
import sys

def help():
    print(""" Usage: cloud_backup [COMMAND]

    Commands:
        status - Show current status of cron backup
        create_backup - Create the Backup targets and put on cron 
        create_database_backup - Create the Backup of Database target and put on cron 
        syncronize - Send backups to cloud """)

def main():
    drive = Drive()
    drive.set_up()

    folder_id = drive.get_folder()

    command = sys.argv[1] if len(sys.argv) > 1 else  None
    
    if command == "help":
        help()
    elif command == "create_backup":
        CreateBackup().run_setup()
    elif command == "create_database_backup":
        CreateDatabaseBackup().run_setup()
    elif command == "syncronize":
        Syncronize().run()
    else:
        print(Status().format())
        



if __name__ == '__main__':
    main()