# Agenda Convert
This program aims to convert agenda in .xls type to a searchable table using python sqlite.

## Import Agenda
This program imports the schedule of an event into a local SQLite database.

1. Open an Agenda excel file
2. Design a SQLite Database table schema allowing to store agenda information
3. Parse the content of the excel file and store the content in the table you designed

Run your program as follow:
$python ./import_agenda.py agenda.xls

Please note:
* The input file needs to follow the same format as the one provided in this repository. (For example, start at line 15)



## Lookup Agenda
This program finds agenda sessions in the data you imported.

1. Parse the command line arguments to retrieve the conditions that the sessions we are looking for must match.
2. Lookup the data you imported for the matching records
3. Print the result onto the screen

Run your program as follow:
$Python ./lookup_agenda.py column value

Where:
* column can be one of {date, time_start, time_end, title, location, description, speaker}
* value is the expected value for that field

For example, if I got the following simplified rows:
Title	     Location 	  Description		    Type
===========================================================================
Breakfast    Lounge	  Fresh fruits and pastries Session
Hangout	     Beach	  Have fun		    Subsession of Breakfast
Lunch	     Price Center Junk food    	   	    Session
Dinner	     Mamma Linnas Italien handmade pasta    Session
Networking   Lounge	  Let's meet		    Subsession of Dinner

Then the expected behavior is as follow:
$python ./lookup_agenda.py location lounge
Breakfast   Lounge    	  Fresh fruits and pastries Session	  # Returned because its location is lounge 
Hangout	    Beach	  Have fun		    Subsession    # Returned because its parent session location is lounge
Networking  Lounge	  Let's meet   	   	    Subsession	  # Returned because its location is lounge

Please note:
* Program looks for sessions and subsessions
* If one of the matched session has any subsession, it will return all the subsessions belonging to that session as well
* It prints out all the information about the right sessions.
* The program looks for an exact match for date, time_start, time_end, title, location and description.
* For speaker, only pass one name at a time. Expect all sessions where we can find this speaker, even though he may not be the only speaker.


## db_table.py
This file provides a basic wrapper around the SQLite3 database and provides features such as:
* create table
* select
* insert
* update


## agenda.xls
This is the file you are supposed to import for the "Import Agenda" program.


## Resources
* [Python SQLite3 documentation](https://docs.python.org/2/library/sqlite3.html)
* [Python Excel parsing](https://github.com/python-excel/xlrd)
