#from crypt import methods
from urllib import request
from emp_model import emp_model
from flask import request
from flask import Flask
from flask_cors import CORS

app=Flask(__name__)
# CORS(app, resources=r'/api/*')
CORS(app, resources={r"*": {"origins": "*"}})

obj = emp_model() 

@app.route('/')
def index():
    return "Hello World"


@app.route("/employee")
def user_getall_controller():
    return obj.emp_getall_model()


@app.route("/employee/<id>" )
def user_getemployee_controller(id):
    return obj.emp_getemployee_model(id)

@app.route("/employee/addone", methods=["POST"])
def user_addone_controller():
    return obj.emp_addone_model(request.json)

@app.route("/employee/update", methods=["PUT"])
def user_update_controller():
    return obj.emp_update_model(request.json)

@app.route("/employee/delete/<id>", methods=["DELETE"])
def user_delete_controller(id):
    return obj.emp_delete_model(id)


if __name__=="__main__":
    app.run(debug=True)