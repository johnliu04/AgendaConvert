#!/usr/bin/python
import sys
import xlrd
import db_table

#
#Create an empty table
#
agenda = db_table.db_table("agenda", {"id": "integer", 
                                    "date": "text",
                                    "time_start": "text",
                                    "time_end": "text",
                                    "title": "text",
                                    "location": "text",
                                    "description": "text",
                                    "speaker": "text"}) 


if __name__ ==  '__main__':
    #Check argument
    try:
        file = str(sys.argv[1])
        file_data = xlrd.open_workbook(file).sheet_by_index(0)
        id_curr = 1
        for i in range(15, file_data.nrows):
            date = file_data.cell_value(i, 0).replace("'", "")
            time_start = file_data.cell_value(i, 1).replace("'", "")
            time_end = file_data.cell_value(i, 2).replace("'", "")
            id = id_curr
            if file_data.cell_value(i, 3) == "Session":
                id_curr += 1
            elif file_data.cell_value(i, 3) == "Sub":
                id = id_curr - 1
            id_str = str(id)
            title = file_data.cell_value(i, 4).replace("'", "")
            location = file_data.cell_value(i, 5).replace("'", "")
            description = file_data.cell_value(i, 6).replace("'", "")
            speaker = file_data.cell_value(i, 7).replace("'", "")
            
            agenda.insert({"id": id_str, 
                            "date": date,
                            "time_start": time_start,
                            "time_end": time_end,
                            "title": title,
                            "location": location,
                            "description": description,
                            "speaker": speaker})
        print("Imported")
    except IndexError:
        print("CAN NOT IMPORT AGENDA!\nPlease run the program as follow: '$python ./import_agenda.py agenda.xls'")

    