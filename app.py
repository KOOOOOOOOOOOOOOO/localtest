from flask import Flask, render_template, jsonify, request
import pymysql
from flask_restful import Resource, Api
from flask_mysqldb import MySQL,MySQLdb
import json



app = Flask(__name__)
app.secret_key = "gucciruable"


app.config ['MYSQL_HOST'] = 'localhost'
app.config ['MYSQL_USER'] = 'root'
app.config ['MYSQL_PASSWORD'] = 'stanley1913!'
app.config ['MYSQL_DB'] = 'aptInfo'
app.config ['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

#@app.route('/')
#def get_db():
    # cursor = mysql.connection.cursor()
    # cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # cur.execute("SELECT * FROM apt ORDER BY id ASC")
    # apt = cur.fetchall()

    # return render_template('index.html', apt=apt)

@app.route('/')
def indexing():
    return render_template('index.html')

@app.route('/action')
def action_page():
    return render_template('action.html')


if __name__ == '__main__':
    app.run(debug=True)
