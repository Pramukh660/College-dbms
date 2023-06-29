import psycopg2
import psycopg2.extras

config = {
    'host': 'ap-south-1.cb9b7641-8427-4775-afbb-3ce527f635ee.aws.ybdb.io',
    'port': '5433',
    'dbName': 'yugabyte',
    'dbUser': 'admin',
    'dbPassword': '3aSbVrpXXcxuS3aexM-3yDQA5z3j8-',
    'sslMode': 'verify-full',
    'sslRootCert': "https://github.com/Pramukh660/College-dbms/blob/main/root.crt"
}

def main(conf):
    print(">>>> Connecting to YugabyteDB!")

    try:
        if conf['sslMode'] != '':
            yb = psycopg2.connect(host=conf['host'], port=conf['port'], database=conf['dbName'],
                                  user=conf['dbUser'], password=conf['dbPassword'],
                                  sslmode=conf['sslMode'], sslrootcert=conf['sslRootCert'],
                                  connect_timeout=5)
        else:
            yb = psycopg2.connect(host=conf['host'], port=conf['port'], database=conf['dbName'],
                                  user=conf['dbUser'], password=conf['dbPassword'],
                                  connect_timeout=5)
    except Exception as e:
        print("Exception while connecting to YugabyteDB")
        print(e)
        exit(1)

    print(">>>> Successfully connected to YugabyteDB!")
    return yb

# Connect to YugabyteDB
yb = main(config)
yb.set_session(autocommit=True)
yb_cursor = yb.cursor()

# Create the Professors table
# yb_cursor.execute('DROP TABLE IF EXISTS Professors;')
yb_cursor.execute("CREATE TABLE Professors ("
               "professor_id SERIAL4 PRIMARY KEY,"
               "name VARCHAR(100),"
               "contact VARCHAR(100),"
               "department_id INT);")

# Create the Departments table
# yb_cursor.execute('DROP TABLE IF EXISTS Departments CASCADE;')
yb_cursor.execute("CREATE TABLE Departments ("
               "department_id SERIAL4 PRIMARY KEY,"
               "name VARCHAR(100));")

# Create the Courses table
# yb_cursor.execute('DROP TABLE IF EXISTS Courses;')
yb_cursor.execute("CREATE TABLE Courses ("
               "course_id SERIAL4 PRIMARY KEY,"
               "name VARCHAR(100),"
               "department_id INT,"
               "FOREIGN KEY (department_id) REFERENCES Departments(department_id));")

# Create the Students table
# yb_cursor.execute('DROP TABLE IF EXISTS Students;')
yb_cursor.execute("CREATE TABLE Students ("
               "student_id SERIAL4 PRIMARY KEY,"
               "name VARCHAR(100),"
               "contact VARCHAR(100),"
               "major VARCHAR(100));")

# Close the cursor and database connection
yb_cursor.close()
yb.close()