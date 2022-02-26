#!/usr/bin/python
from re import S
import sys
import import_agenda


def search(column, value):
    results = []
    if(column == "speaker"):
        searches = import_agenda.speaker.select(where = {"person": value})
    else:
        searches = import_agenda.agenda.select(where = {column: value})
    for search in searches:
        temp1 = [x for x in search.values()]
        if temp1[1] == "Session":
            tasks = import_agenda.agenda.select(where = {"id": temp1[0]})
            #print(len(tasks))
            for task in tasks:
                temp2 = [y for y in task.values()]
                results.append(temp2)
        elif temp1[1] == "Sub":
            results.append(temp1)
    return results

def print_result_table(results):
    for result in results:
        #Required Fields*: Session Title, Date, Time Start, Time End, Session
        print("Date: " + result[2])
        print("Time Start: " + result[3])
        print("Time End: " + result[4])
        print("Session or Sub-session(Sub): " + result[1])
        print("Session Title: " + result[5])
        print("Room/Location: " + result[6])
        print("Description: " + result[7])
        print("Speakers: " + result[8])
        print("--------------------------------------------------------")
    print("Finished! Found " + str(len(results)) + " results as above.")

if __name__ ==  '__main__':
    try:
        column = str(sys.argv[1])
        value = str(sys.argv[2])
        if column not in ["date", "time_start", "time_end", "title", "location", "description", "speaker"]:
            raise ValueError("Column input error!\ncolumn can be one of {date, time_start, time_end, title, location, description, speaker}")
        results = search(column, value)
        if(len(results) > 0):
            print_result_table(results)
        else:
            print("--------------------------------------------------------")
            print("RESULTS NOT FOUND!")
        
    except IndexError:
        print("CAN NOT LOOKUP AGENDA!\nPlease run the program as follow: '$python ./lookup_agenda.py column value'")
