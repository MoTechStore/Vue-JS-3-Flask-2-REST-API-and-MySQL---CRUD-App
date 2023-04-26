from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_mysqldb import MySQL 
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'test' 

mysql = MySQL(app)

api = Api(app)



def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


class Student(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM students")
        data = dictfetchall(cur)
        cur.close()
        print(type(data))

        return jsonify({'students':data,'Method':'GET'})


    def post(self):
        data = request.get_json()
        print(data)
        name = data['name']
        email = data['email']
        course = data['course']
        gender = data['gender']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (name,course,email,gender) VALUES(%s, %s, %s, %s)", (name,course,email,gender))

        return jsonify({'Method':'POST', 'message':'New student created successfully'})


    def put(self):
        data = request.get_json()
        print(data)
        id = data['id']
        name = data['name']
        email = data['email']
        course = data['course']
        gender = data['gender']

        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE students SET name=%s, course=%s, email=%s, gender=%s
        WHERE id=%s 
        """, (name,course,email,gender,id))

        return jsonify({'Method':'PUT', 'message':'Student updated successfully'})

    def patch(self):
        data = request.get_json()
        print(data)
        id = data['id']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM students WHERE id=%s", (id,))
        mysql.connection.commit()


        return jsonify({'Method':'PATCH', 'message':'Student daeleted successfully'})            


api.add_resource(Student, '/api/students/')

if __name__ == '__main__':
    app.run(debug=True)
