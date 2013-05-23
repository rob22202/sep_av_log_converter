sep_av_log_converter
====================

Python script used to make the AppData\Symantec\....\Logs\AV\*.log files readable through date conversion and event code lookup.

The main script, sep_av_log_converter.py, requires the sep_codes.db sql lite database reside in the same directory.  The database is created by first running the create_sep_codes_db.py script.

It will convert only one log file at a time and automatically renames it to <original_name.log>.converted.csv.

Let me know if you come up with any good enhancement ideas or modifications.

- rob22202@gmail.com
