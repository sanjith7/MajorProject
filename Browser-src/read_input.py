import csv
#Open file with "w"(write), the file will create automatically.
file = open(r'C:\xampp\htdocs\HealthKeeper\RPi\Worker\data.txt', "w")
#Open CSV file to read CSV, note: reading and write file should be under "with"
with open('/Users/sanji/Desktop/mp/arima_input_datafiles/data10.csv') as csvFile:
    #Read CSV
    readCsv = csv.reader(csvFile)
    for row in readCsv:
        #Get Values and manupilate in the file.write
        Id = row[0]
        Id1 = row[1]
        print(Id)
        #Write CSV you need format it to string if the value is an int
        # file.write("UPDATE Schema.TableName SET Column1="+str(Id1)+" where Column2="+str(Id)+";\n")
#You Must Close the FIle after writing it.
file.close()