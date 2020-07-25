import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:localhost,1433' 
database = 'msdb' 
username = 'sa' 
password = '11qq@@WW' 

try:
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
except:
    print("Failed to connect...")
finally:
    if cnxn:
        print("Connected to MySQL Server version: ")
        cursor.execute("SELECT @@version;") 
        row = cursor.fetchone() 
        while row: 
            print(row[0])
            row = cursor.fetchone()
    else:
        print("DB no running yet")




