from flask import Flask, jsonify
import mysql.connector




app = Flask(__name__)

def conn():
    mydb = mysql.connector.connect(
      host="mysqlhost",
      user="root",
      password="password123"
    )
    return mydb



@app.route('/')
def hello_world():

    return 'Hello, World!!!!!!!!'


@app.route('/list_all')
def list_all_users():

    sql = "SELECT fname, lname, username, password FROM mangodb.users"
    db = conn()
    cur = db.cursor(dictionary=True)
    cur.execute(sql)

    result = cur.fetchall()

    return jsonify(result)


@app.route('/login')
def login_function():

    return 'This is a login page'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
