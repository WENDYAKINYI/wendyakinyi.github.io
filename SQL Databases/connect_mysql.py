import mysql.connector


class DBTest:
    def __init__(self):
        # Establish the connection to the MySQL database
        self.mydb = mysql.connector.connect(
            user='root',
            passwd='Mogad1shu*#',
            database='comp3421',
            host='127.0.0.1',
            allow_local_infile=1
        )
        self.mycur = self.mydb.cursor()

    def close(self):
        # Commit any changes (if applicable) and close the connection
        self.mydb.commit()
        self.mycur.close()  # Close the cursor
        self.mydb.close()   # Close the database connection

    def getCandy(self):
        # Perform the query
        sql = "SELECT cust_id, cust_name FROM candy_customer LIMIT 4"
        self.mycur.execute(sql)

        # Display the results
        results = []  # List to hold results
        for row in self.mycur:
            cust_id = row[0]
            name = row[1]
            # Append results to the list
            results.append(f"custID: {cust_id}, name: {name}")
            print(f"custID: {cust_id}, name: {name}")  # Print each result

        return results  # Return the list of results

    def createJunkTable(self):
        # Create a table called 'junk' with an auto-incremented primary key
        sql = '''
        CREATE TABLE IF NOT EXISTS junk (
            junkid INT AUTO_INCREMENT PRIMARY KEY,
            junk_data VARCHAR(255)
        )
        '''
        self.mycur.execute(sql)
        self.mydb.commit()
        print("Table 'junk' created successfully.")

    def insertIntoJunk(self):
        # Insert one row into the 'junk' table
        sql = "INSERT INTO junk (junk_data) VALUES ('Some junk data')"
        self.mycur.execute(sql)
        self.mydb.commit()
        print("Row inserted into 'junk' table.")

    def dropJunkTable(self):
        # Drop the 'junk' table
        sql = "DROP TABLE IF EXISTS junk"
        self.mycur.execute(sql)
        self.mydb.commit()
        print("Table 'junk' dropped successfully.")


# Testing code
if __name__ == "__main__":
    test = DBTest()  # Create an instance of DBTest
    test.getCandy()  # Call the getCandy method to retrieve and print data
    test.createJunkTable()  # Create the 'junk' table
    test.insertIntoJunk()  # Insert a row into the 'junk' table
    test.dropJunkTable()  # Drop the 'junk' tabletest.dropJunkTable()  # Drop the 'junk' table
    test.close()  # Close the database connection
