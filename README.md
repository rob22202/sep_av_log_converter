sep_av_log_converter
====================

Python script used to make the AppData\Symantec\....\Logs\AV\*.log files readable through date conversion and event code lookup.

The script requires the sep_codes.db sql lite database reside in the same directory.

It will convert only one log file at a time and automatically renames it to <original_name.log>.converted.csv.

Let me know if you come up with any good enhancement ideas or modifications.

- rob22202@gmail.com
