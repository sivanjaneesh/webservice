import mysql.connector
import json
import flask
from flask import jsonify
class emp_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="34.28.138.189",user="root",password="",database="employee")
            self.con.autocommit=True
            self.cur = self.con.cursor(dictionary=True)
            print('Connection Successful')
        except:
            print("Some error")
    def emp_getall_model(self):
        self.cur.execute("SELECT * FROM employee")
        result=self.cur.fetchall()
        if len(result)>0:
            return jsonify(result)
        else:
            return {"message" :"No Data Found"}
    
    def emp_getemployee_model(self,id):
        self.cur.execute(f"SELECT * FROM employee where PersonID={id}")
        result=self.cur.fetchall()
        if len(result)>0:
            return jsonify(result)
        else:
            return {"message":"No data found"}

    def emp_addone_model(self,data):
        self.cur.execute(f"INSERT INTO employee(FirstName, LastName, Address, City) VALUES('{data['FirstName']}','{data['LastName']}','{data['Address']}','{data['City']}')")
        return {"message" :"User Created Successfully"}
    
    def emp_update_model(self,data):
        self.cur.execute(f"UPDATE employee SET FirstName='{data['FirstName']}',LastName='{data['LastName']}',Address='{data['Address']}',City='{data['City']}' WHERE PersonID={data['id']}")
        if self.cur.rowcount>0:
            return {"message" :"User Updated Successfully"}
        else:
            return {"message" :"Nothing to Update"}
        
    def emp_delete_model(self,id):
        self.cur.execute(f"DELETE FROM employee WHERE PersonID={id}")
        if self.cur.rowcount>0:
            return {"message" :"User Deleted Successfully"}
        else:
            return {"message" :"Nothing to Delete"}
