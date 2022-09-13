from flask import Flask,request
import Stud_Helper
inputHandler = Stud_Helper.MySQLHandler
from flask_restful import Resource,Api
students = []
from flask import Flask
from flask_cors import CORS
import json
# Create environment variables for python api
app = Flask(__name__)
CORS(app)

# To get Student data from Database
class Student(Resource):
    def get(self):
     students=inputHandler.displayStud()
    #  json.dumps([{"name": students[0], "id": students[1],"age":students[2]} for student in students])
     print(students)
     return (students)
     
# To Sort Student data by ID
class Student_Sort(Resource):
    def get(self):
     students=inputHandler.sortID()
     
     print(students)
     return (students)

# To Sort Student data by NAME
class StudentSort_Name(Resource):
    def get(self):
     students=inputHandler.sortName()
     print(students)
     return (students)


# app = Flask(__name__)
api = Api(app)
api.add_resource(Student,'/student')
api.add_resource(Student_Sort,'/studentSort')
api.add_resource(StudentSort_Name,'/studentSortName')

# To Insert data in Database
@app.route('/add_student', methods=['POST'])
def process_json():
     content_type = request.headers.get('Content-Type')
     if (content_type == 'application/json'):
         json = request.json
         print(json)
         name = request.json['name']
         id = request.json['id']
         age = request.json['age']
         print(name,id,age)
         inputHandler.insertJson(name,id,age)
        
         return json
     else:
         return 'Content-Type not supported!'

# To Delete data from Database
@app.route('/delete_student', methods=['DELETE'])
def processDel_json():
     content_type = request.headers.get('Content-Type')
     if (content_type == 'application/json'):
         json = request.json
         print(json)
         id = request.json['id']
         print(id)
         inputHandler.deleteJson(id)
        
         return json
     else:
         return 'Content-Type not supported!'

# To Search data ny Name in Database
@app.route('/search_student', methods=['GET'])
def processSearch_json():
     content_type = request.headers.get('Content-Type')
     if (content_type == 'application/json'):
         json = request.json
        #  print(json)
         
         name = request.json['name']
         if(type(name) in (list,tuple)):
            s = []
            for x in name:
                s.append(inputHandler.searchJson(x))
            return s
         else:
            students=inputHandler.searchJson(name)
            return students
        #  print(name)
         
        
         
     else:
         return 'Content-Type not supported!'

# To Update data in Database
@app.route('/update_student', methods=['PATCH'])
def processUpdate_json():
     content_type = request.headers.get('Content-Type')
     if (content_type == 'application/json'):
         json = request.json
         print(json)
         id = request.json['id']
         name = request.json['name']
         print(id,name)
         inputHandler.updateJson(id,name)
        
         return json
     else:
         return 'Content-Type not supported!'


if __name__ == '__main__':
    app.run()
