#!/usr/bin/python
import sys
import xlrd
import db_table

#
# Create an empty table
#
agenda = db_table.db_table("agenda", {"id": "integer", 
                                    "type":"text",
                                    "date": "text",
                                    "time_start": "text",
                                    "time_end": "text",
                                    "title": "text",
                                    "location": "text",
                                    "description": "text",
                                    "speaker": "text"}) 
#
# Create an empty table, which allows replicated info, used for search specific speaker
#  (Works, but wasted storage. May need to be upgraded.)
#                                   
speaker = db_table.db_table("speaker", {"id": "integer", 
                                    "type":"text",
                                    "date": "text",
                                    "time_start": "text",
                                    "time_end": "text",
                                    "title": "text",
                                    "location": "text",
                                    "description": "text",
                                    "speaker": "text",
                                    "person":"text"})

if __name__ ==  '__main__':
    # Check argument
    try:
        file = str(sys.argv[1])
        file_data = xlrd.open_workbook(file).sheet_by_index(0)
        # Error caused by apostrophe while dealing with stirng.
        #  (Solved by replace ' by ~, which is not used in .xls file, but may cause error in other circumstances)
        id_curr = 1
        for i in range(15, file_data.nrows):
            date = file_data.cell_value(i, 0).replace("'", "~")
            time_start = file_data.cell_value(i, 1).replace("'", "~")
            time_end = file_data.cell_value(i, 2).replace("'", "~")
            # Sub-session get the same id number as its session
            id = id_curr
            type = ""
            if file_data.cell_value(i, 3) == "Session":
                id_curr += 1
                type = "Session"
            elif file_data.cell_value(i, 3) == "Sub":
                id = id_curr - 1
                type = "Sub"
            id_str = str(id)
            title = file_data.cell_value(i, 4).replace("'", "~")
            location = file_data.cell_value(i, 5).replace("'", "~")
            description = file_data.cell_value(i, 6).replace("'", "~")
            speakers = file_data.cell_value(i, 7).replace("'", "~")
            persons = speakers.split("; ")
            for person in persons:
                speaker.insert({"id": id_str, 
                                "type": type,
                                "date": date,
                                "time_start": time_start,
                                "time_end": time_end,
                                "title": title,
                                "location": location,
                                "description": description,
                                "speaker": speakers,
                                "person": person})
            
            agenda.insert({"id": id_str, 
                            "type": type,
                            "date": date,
                            "time_start": time_start,
                            "time_end": time_end,
                            "title": title,
                            "location": location,
                            "description": description,
                            "speaker": speakers})
        print("Agenda Table Imported!")
    except IndexError:
        print("CAN NOT IMPORT AGENDA!\nPlease run the program as follow: '$python ./import_agenda.py agenda.xls'")

    