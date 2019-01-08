# CloudBackup

Working with Backups can be tedius and difficult, `CloudBackup` permit the developer to work without any downside

## How Work

CRON is used to call daily tasks of `CloudBackup` to Syncronize in cloud and make new backups, every day 

* You can change the routine in `/commands/create_backup.py` and `/commands/create_database_backup.py`

## Installing

* Clone the repo
* Install requisits 
```bash
pip install -r requirements.txt
```
* Done

## In first run

Only in the first run you be requisited to authorize you `GoogleDrive` to accept the files being sent to it

## Using

```bash
python cloud_backup.py help # Show the help
```

```bash
python cloud_backup.py create_backup # Create Directory Backup in tar.gz
```

```bash
python cloud_backup.py create_database_backup # Create the database backup in SQL
```

```bash
python cloud_backup.py syncronize # Send the files to cloud
```

```bash
python cloud_backup.py status # Check active CRON configuration for the user
```

* When you run without additionals arguments you will be asked to enter information as database name or source directory to backup, so, you can run only the commands above or run all in one line, you choose


## Anything, just open a Issue or send me a message