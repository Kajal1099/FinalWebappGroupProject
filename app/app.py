from flask import Flask, Markup, render_template, request, Response, redirect
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
import simplejson as json

app = Flask(__name__)

mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'charts'
mysql.init_app(app)

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
    app.run(host='0.0.0.0', port=5000)