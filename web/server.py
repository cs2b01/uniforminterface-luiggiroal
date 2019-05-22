from flask import Flask, render_template, request, session, Response, redirect
from database import connector
from model import entities
from flask_bootstrap import Bootstrap
import json

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Root page
@app.route('/')
def main():
	return render_template('index.html')

# Get all students
@app.route('/students', methods = ['GET'])
def get_all_students():
	db_session = db.getSession(engine)
	students = db_session.query(entities.Student)
	data = students[:]
	return Response(json.dumps(data, cls= connector.AlchemyEncoder), mimetype = 'application/json')

# Set students

# Once the list of students is set, repeating the setting
# process will cause an error due to the 'id' entity is a 
# primary key and can't be repeated in the table. 
# In the following presentations a 'delete' and 'update' view function
# will be implemented in order to solve this problem.
@app.route('/setStudents', methods = ['GET'])
def set_students():
    db_session = db.getSession(engine)
    student1 = entities.Student(id = 100, name = 'Robert', lname = 'Smith', uname = 'rsmith', password = '101')
    student2 = entities.Student(id = 200, name = 'Tom', lname = 'Yorke', uname = 'tyorke', password = '102')
    db_session.add(student1)
    db_session.add(student2)
    db_session.commit()
    return "Students created!"

if __name__ == '__main__':
    app.secret_key = ".."
app.run(port=8080, threaded=True, host=('0.0.0.0'), debug = True)