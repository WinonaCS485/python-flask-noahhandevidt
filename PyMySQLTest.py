import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='xw5214bs',
                             password='HarrisonSmith22',
                             db='xw5214bs_UniversityDB',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

userInput = input("What first name are you searching for? ")

try:
    with connection.cursor() as cursor:
        # Select all Students
        sql = "SELECT * FROM Student WHERE FirstName = '" + userInput + "'"
        
        # execute the SQL command
        cursor.execute(sql)
        
        # get the results
        for result in cursor:
            print (result)
        
      
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes. 
        # connection.commit()
        

finally:
    connection.close()
