import psycopg2.extras
from flask import Flask, render_template, request

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
    # print(">>>> Connecting to YugabyteDB!")

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

    # print(">>>> Successfully connected to YugabyteDB!")
    return yb

# Connect to YugabyteDB
yb = main(config)
yb.set_session(autocommit=True)
yb_cursor = yb.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/professors')
def professors():
    yb_cursor = main(config).cursor()
    yb_cursor.execute("SELECT * FROM Professors")
    professors = yb_cursor.fetchall()
    yb_cursor.close()
    return render_template('professors.html', professors=professors)

@app.route('/departments')
def departments():
    yb_cursor = main(config).cursor()
    yb_cursor.execute("SELECT * FROM Departments")
    departments = yb_cursor.fetchall()
    yb_cursor.close()
    return render_template('departments.html', departments=departments)

@app.route('/courses')
def courses():
    yb_cursor = main(config).cursor()
    yb_cursor.execute("SELECT * FROM Courses")
    courses = yb_cursor.fetchall()
    yb_cursor.close()
    return render_template('courses.html', courses=courses)

@app.route('/students')
def students():
    yb_cursor = main(config).cursor()
    yb_cursor.execute("SELECT * FROM Students")
    students = yb_cursor.fetchall()
    yb_cursor.close()
    return render_template('students.html', students=students)

if __name__ == "__main__":
    main(config)
    app.run(debug=True)