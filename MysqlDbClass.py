#David Fry
#6-20-13

import MySQLdb

class Database(object):
    
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.database)
    
    def execute_query(self, q):
        """ Executes the query sting and then commits it to the database, uses the DictCursor
            becasue you can use a name vs a number to index.
            IE: record['name'] instead of record[0]
            
            execute_query(string) --> string
            
            EXMPLE:
            >>> execute_query('CREATE TABLE tblName')
        """
        cur = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute(q)
        self.connection.commit()
        return cur.fetchall()
    
    def create_table(self, table_name, fields):
        """ Creates a table in your database from the query string and
            returns a the full query string. You need to provide
            the field names and type in the fields variable.
            
            create_table(string, string) --> string
            
            EXAMPLE:
            >>> create_table('tblName', 'name TYPE ANY OTHER PARAMETERS' )

        """
        query = "CREATE TABLE " + table_name + "(" + fields + ")"
        self.execute_query(query)
        return query
    
    def insert_into_table(self, table_name, fields, data):
        """ Inserts data into the specified table rows.
            The data variable holds the data for inserting.
            return the full query string.
            
            insert_into_table(string, string, string) --> string
            
            EXAMPLE:
            >>> insert_into_table('tblName', 'name, age, date', ('jonny', '30', '6-24-2013'))

        """
        query = "INSERT INTO " + table_name + "(" + fields + ")" + " VALUES " + data
        self.execute_query(query)
        return query
    
    def delete_table(self, table_name):
        """ Deletes the specfied table from the database.
            WARNING: This will also delete all of the records in
            the table. return the full query string
            
            delete_table(string) --> string
            
            EXAMPLE:
            >>> delete_table('tblName')
        """
        query = "DROP TABLE " + table_name
        self.execute_query(query)
        return query
    
    
    def __del__(self):
        self.connection.close()
