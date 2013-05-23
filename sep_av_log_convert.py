#!/usr/bin/python

import csv, sqlite3, sys, getopt

def main(argv):
        inputfile = ''
        outputfile = ''

        try:
                opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
        except getopt.GetoptError:
                print 'sep_av_log_convert.py -i <inputfile>'
                sys.exit(2)

        for opt, arg in opts:
                if opt == '-h':
                        print 'sep_av_log_convert.py -i <inputfile>'
                        sys.exit()
                elif opt in ("-i", "--ifile"):
                        inputfile = arg
                elif opt in ("-o", "--ofile"):
                        outputfile = arg

        if inputfile == "":
                print "Usage: sep_av_log_convert.py -i <inputfile>"
                print "No input file specified"
                print ""
                sys.exit(2)

        outputfile=inputfile+".converted.csv"

        conn = sqlite3.connect("sep_codes.db")
        cursor = conn.cursor()

        print ""
        print "Converting:  " + inputfile
        print "Outputting: " + outputfile
        print "Inserting SEP Event Event Codes from ./sep_codes.db SQLite3 Database"
        print ""

        new_rows = []

        with open(inputfile, 'rb') as input_csv:
                reader = csv.reader(input_csv)
                for row in reader:
                        new_row = row
                        ctime = row[0]
                        new_row[0] = convert_ctime(ctime)
                        event_code = row[1]

                        sql = "select event from sep_codes where code = ?"
                        lookup = cursor.execute(sql, [(event_code)]).fetchone()
                        if lookup is not None:
                                new_row[1] = lookup[0]+" ("+event_code+")"
                        new_rows.append(new_row)

        with open (outputfile, 'wb') as output_csv:
                writer = csv.writer(output_csv)
                writer.writerows(new_rows)

def convert_ctime(ctime):
        year = str(int(ctime[:2],16)+1970)
        month = str(int(ctime[2:4],16))
        day = str(int(ctime[4:6],16))
        hour = str(int(ctime[6:8],16))
        minute = str(int(ctime[8:10],16))
        second = str(int(ctime[10:12],16))
        return month+"/"+day+"/"+year+" "+hour+":"+minute+":"+second

if __name__ == "__main__":
        main(sys.argv[1:])
