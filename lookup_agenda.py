#!/usr/bin/python
from re import S
import sys
from tkinter import font
import import_agenda
import xlwt


def search(column, value):
    results = []
    # Use speaker table to search if the column is speaker
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
        print("Date: " + result[2].replace("~","'"))
        print("Time Start: " + result[3].replace("~","'"))
        print("Time End: " + result[4].replace("~","'"))
        print("Session or Sub-session(Sub): " + result[1].replace("~","'"))
        print("Session Title: " + result[5].replace("~","'"))
        print("Room/Location: " + result[6].replace("~","'"))
        print("Description: " + result[7].replace("~","'"))
        print("Speakers: " + result[8].replace("~","'"))
        print("--------------------------------------------------------")
    print("Finished! Found " + str(len(results)) + " results as above.")

def export_xsl(results):
    book = xlwt.Workbook()
    sheet = book.add_sheet("Results", cell_overwrite_ok = True)
    sheet.write(14, 0, label = "Date")
    sheet.write(14, 1, label = "Time Start")
    sheet.write(14, 2, label = "Time End")
    sheet.write(14, 3, label = "Session or Sub-session(Sub)")
    sheet.write(14, 4, label = "Session Title")
    sheet.write(14, 5, label = "Room/Location")
    sheet.write(14, 6, label = "Description")
    sheet.write(14, 7, label = "Speakers")
    row = 15
    for result in results:
        sheet.write(row, 0, label = result[2])
        sheet.write(row, 1, label = result[3])
        sheet.write(row, 2, label = result[4])
        sheet.write(row, 3, label = result[1])
        sheet.write(row, 4, label = result[5])
        sheet.write(row, 5, label = result[6])
        sheet.write(row, 6, label = result[7])
        sheet.write(row, 7, label = result[8])
        row += 1
    book.save("results.xls")
    

if __name__ ==  '__main__':
    try:
        column = str(sys.argv[1])
        value = str(sys.argv[2])
        value = value.replace("'","~")
        # check if column is valid as stated in guidelines
        if column not in ["date", "time_start", "time_end", "title", "location", "description", "speaker"]:
            raise ValueError("Column input error!\ncolumn can be one of {date, time_start, time_end, title, location, description, speaker}")
        results = search(column, value)
        print("--------------------------------------------------------")
        if(len(results) > 0):
            print_result_table(results)
            export_xsl(results)
        else:
            print("RESULTS NOT FOUND!")
        
    except IndexError:
        print("CAN NOT LOOKUP AGENDA!\nPlease run the program as follow: '$python ./lookup_agenda.py column value'")
