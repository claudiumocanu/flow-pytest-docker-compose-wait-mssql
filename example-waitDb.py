import pyodbc
import time
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:localhost,1433' 
database = 'msdb' 
username = 'sa' 
password = '11qq@@WW' 

def waitDb(server, database, username, password, maxAttempts, waitBetweenAttemptsSeconds):
    for attemptNumber in range(maxAttempts):
        cnxn = None
        try:
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            cursor = cnxn.cursor()
        except:
            print("Failed to connect...")
        finally:
            if cnxn:
                print("The DB is up and running: ")
                cursor.execute("SELECT @@version;") 
                row = cursor.fetchone() 
                while row: 
                    print(row[0])
                    row = cursor.fetchone()
                return True
            else:
                print("DB no running yet on attempt numer " + str(attemptNumber))
            time.sleep(waitBetweenAttemptsSeconds)
    print("Max attempts waiting for DB to come online exceeded")
    return False



waitDb(server, database, username, password, 3, 5)

