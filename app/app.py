from typing import List, Dict
import simplejson as json
from flask import Flask, request, Response, redirect
from flask import render_template, Markup
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
from sendemail import sendemail
import sys
from datetime import datetime
import random

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'clsStudents'
mysql.init_app(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('login.html', title='Login Page')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html', title='Login Page')

@app.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html', title='SignUp Page')

@app.route('/index', methods=['GET'])
def show_index():
    user = {'username': 'Kajal and Abhay'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM cls_students')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, students=result)

@app.route('/logins/new', methods=['POST'])
def add_login():
    cursor = mysql.get_db().cursor()
    strEmail = str(request.form.get('email'))

    cursor.execute('SELECT * FROM tblUsers WHERE userEmail=%s', strEmail)

    row_count = cursor.rowcount
    if row_count == 0:
        strPassword = request.form.get('pswd')
        strName = request.form.get('name')
        print('No rows returned', file=sys.stderr)
        random.seed(datetime.now())
        strHash = str(random.randint(123234, 1232315324))
        inputData = (strName, strEmail, strPassword, strHash)
        sql_insert_query = """INSERT INTO tblUsers (userName,userEmail,userPassword,userHash) 
                VALUES (%s, %s,%s, %s) """
        cursor.execute(sql_insert_query, inputData)
        mysql.get_db().commit()
        sendemail.sendemail(strEmail, strHash)
        return render_template('login.html', title='Login Page')
    else:
        print('Login already exists', file=sys.stderr)
        cursor.execute('SELECT * FROM tblErrors where errName=%s', 'USER_EXISTS')
        result = cursor.fetchall()
        return render_template('notify.html', title='Notify', student=result[0])

@app.route('/checklogin', methods=['POST'])
def form_check_login():
    strEmail = str(request.form.get('email'))
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblUsers WHERE userEmail=%s', strEmail)
    row_count = cursor.rowcount
    if row_count == 0:
        print('No rows returned', file=sys.stderr)
        cursor.execute('SELECT * FROM tblErrors where errName=%s', 'USER_NOT_FOUND')
        result = cursor.fetchall()
        return render_template('notify.html', title='Notify', student=result[0])
    else:
        result = cursor.fetchall()

        if result[0]['userHash'] != '':
            print('userHash ' + result[0]['userHash'], file=sys.stderr)
            cursor.execute('SELECT * FROM tblErrors where errName=%s', 'EMAIL_NOT_VERIFIED')
            result = cursor.fetchall()
            return render_template('notify.html', title='Notify', student=result[0])

        if str(result[0]['userPassword']) == str(request.form.get('pswd')):

            user = {'username': str(result[0]['userName'])}
            cursor = mysql.get_db().cursor()
            cursor.execute('SELECT * FROM cls_students')
            result = cursor.fetchall()
            return render_template('index.html', title='Home', user=user, students=result)

        else:
            print('Invalid Id/PWD', file=sys.stderr)
            cursor.execute('SELECT * FROM tblErrors where errName=%s', 'INVALID_LOGIN')
            result = cursor.fetchall()
            return render_template('notify.html', title='Notify', student=result[0])

@app.route('/validateLogin/<int:intHash>', methods=['GET', 'POST'])
def validateLogin(intHash):
        cursor = mysql.get_db().cursor()
        inputData = str(intHash)
        sql_update_query = """UPDATE tblUsers t SET t.userHash = '' WHERE t.userHash = %s """
        cursor.execute(sql_update_query, inputData)
        mysql.get_db().commit()
        cursor.execute('SELECT * FROM tblErrors where errName=%s', 'EMAIL_VERIFIED')
        result = cursor.fetchall()
        return render_template('notify.html', title='Notify', student=result[0])




@app.route('/edit/<int:student_id>', methods=['POST'])
def form_update_post(student_id):
    cursor = mysql.get_db().cursor()
    inputData = (str(request.form.get('Name')), str(request.form.get('Room')), str(request.form.get('Class')),
                 str(request.form.get('Age')), student_id)
    sql_update_query = """UPDATE cls_students t SET t.Name = %s, t.Room = %s, t.Class = %s, t.Age = %s WHERE t.id = %s"""
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)



@app.route('/Names/new', methods=['POST'])
def form_insert_post():
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('Name'), request.form.get('Room'), request.form.get('Class'),
                 request.form.get('Age'))
    sql_insert_query = """INSERT INTO cls_students (Name,Room,Class,Age) 
    VALUES (%s, %s,%s, %s,%s, %s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/delete/<int:student_id>', methods=['POST'])
def form_delete_post(student_id):
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM cls_students WHERE id = %s """
    cursor.execute(sql_delete_query, student_id)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/api/v1/Names', methods=['GET'])
def api_browse() -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM cls_students')
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/Names/<int:student_id>', methods=['GET'])
def api_retrieve(student_id) -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM cls_students WHERE id =%s', student_id)
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp

@app.route('/api/v1/Names/<int:student_id>', methods=['PUT'])
def api_edit(student_id) -> str:
    cursor = mysql.get_db().cursor()
    content = request.json
    inputData = (content['Name'], content['Room'], content['Class'],
                 content['Age'], student_id)
    sql_update_query = """UPDATE cls_students t SET t.Name = %s, t.Room = %s, t.Class = %s, t.Age = %s WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp

@app.route('/api/v1/Names/', methods=['POST'])
def api_add() -> str:
    cursor = mysql.get_db().cursor()
    content = request.json
    inputData = (content['Name'], content['Room'], content['Class'],
                 content['Age'])
    sql_insert_query = """INSERT INTO cls_students (Name,Room,Class,Age) 
        VALUES (%s, %s,%s, %s,%s, %s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    resp = Response(status=201, mimetype='application/json')
    return resp

@app.route('/api/v1/Names/<int:student_id>', methods=['DELETE'])
def api_delete(student_id) -> str:
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM cls_students WHERE id = %s """
    cursor.execute(sql_delete_query, student_id)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp

@app.route('/bar')
def bar():
    labels = []
    values = []
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM labels')
    result = cursor.fetchall()
    for label in result:
        labels.append(label["label"])
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM val')
    result = cursor.fetchall()
    for value in result:
        values.append(value["values"])
    bar_labels=labels
    bar_values=values
    return render_template('bar_chart.html', title='Bitcoin Monthly Price in USD', max=17000, labels=bar_labels, values=bar_values)

@app.route('/line')
def line():
    labels = []
    values = []
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM labels')
    result = cursor.fetchall()
    for label in result:
        labels.append(label["label"])
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM val')
    result = cursor.fetchall()
    for value in result:
        values.append(value["values"])
    line_labels=labels
    line_values=values
    return render_template('line_chart.html', title='Bitcoin Monthly Price in USD', max=17000, labels=line_labels, values=line_values)

@app.route('/pie')
def pie():
    labels = []
    values = []
    colors = []
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM labels')
    result = cursor.fetchall()
    for label in result:
        labels.append(label["label"])
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM val')
    result = cursor.fetchall()
    for value in result:
        values.append(value["values"])
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM colors')
    result = cursor.fetchall()
    for color in result:
        colors.append(color["colors"])
    pie_labels = labels
    pie_values = values
    return render_template('pie_chart.html', title='Bitcoin Monthly Price in USD', max=17000, set=zip(values, labels, colors))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
