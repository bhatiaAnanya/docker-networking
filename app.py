import os
from flask import render_template, redirect, request, url_for, flash, session, abort, Flask
from forms import ParamsForm
import mysql.connector
from mysql.connector import Error


def add_user(f_name, l_name):
	connection = mysql.connector.connect(host='localhost',
										database='Users',
										user='root',
										password='Microsoft135&')
	cursor = connection.cursor()

	command = f'''
	INSERT INTO users (first_name, last_name)
	VALUES ("{f_name}", "{l_name}")
	'''

	cursor.execute(command)
	connection.commit()
	cursor.close()
	connection.close()

	print('Added Entry!')	


def get_users():
	connection = mysql.connector.connect(host='localhost',
										database='Users',
										user='root',
										password='Microsoft135&')
	cursor = connection.cursor()
	command  = 'SELECT * FROM users'
	cursor.execute(command)

	result = []
	for (f_name, l_name) in cursor:
		result += [f'{f_name} {l_name}']

	cursor.close()
	connection.close()
	
	return result


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/", methods=['GET', 'POST'])
def main():
	form = ParamsForm()
	if form.validate_on_submit():
		f_name = form.first_name.data
		l_name = form.last_name.data
		add_user(f_name, l_name)
		return redirect(url_for('final'))

	return render_template('index.html', form=form)


@app.route("/final", methods=['GET', 'POST'])
def final():
	users = get_users()
	return str(users)


if __name__ == '__main__':
	app.run(debug=True)
