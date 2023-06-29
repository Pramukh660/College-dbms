import psycopg2
import psycopg2.extras

config = {
    'host': 'ap-south-1.cb9b7641-8427-4775-afbb-3ce527f635ee.aws.ybdb.io',
    'port': '5433',
    'dbName': 'yugabyte',
    'dbUser': 'admin',
    'dbPassword': '3aSbVrpXXcxuS3aexM-3yDQA5z3j8-',
    'sslMode': 'verify-full',
    'sslRootCert': "https://github.com/Pramukh660/College-dbms/main/root.crt"
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

yb_cursor.execute("INSERT INTO Professors (name, contact, department_id) VALUES"
                "('John Smith', 'johnsmith@email.com', 1),"
                "('Emma Johnson', 'emmajohnson@email.com', 2),"
                "('Michael Brown', 'michaelbrown@email.com', 3),"
                "('Sarah Davis', 'sarahdavis@email.com', 4);")

yb_cursor.execute("INSERT INTO Departments (name) VALUES"
                "('English'),"
                "('Mathematics'),"
                "('History'),"
                "('Science');")

yb_cursor.execute("INSERT INTO Courses (name, department_id) VALUES"
                "('Statistics', 2),"
                "('Calculus', 2),"
                "('Literature', 1),"
                "('Chemistry', 4);")

yb_cursor.execute("INSERT INTO Students (name, contact, major) VALUES"
                "('Emily Thompson', 'emilythompson@email.com', 'Mathematics'),"
                "('Ethan Wilson', 'ethanwilson@email.com', 'English'),"
                "('Olivia Clark', 'oliviaclark@email.com', 'History'),"
                "('James Adams', 'jamesadams@email.com', 'Science');")

yb_cursor.close()
yb.close()