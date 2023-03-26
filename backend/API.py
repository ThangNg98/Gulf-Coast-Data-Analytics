import flask
import hashlib
from flask import request, make_response, jsonify
import mysql.connector
from mysql.connector import Error
from sql import create_connection, execute_query, execute_read_query
from datetime import datetime
from flask_cors import CORS

conn = create_connection('172.26.54.22', 'ADMIN', 'password123!', 'llc_database') # connection to database

# setup application
app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

##### returns all the volunteers in the volunteer table ######
@app.route('/', methods = ['GET']) # http://127.0.0.1:5000/
def home():
    
    query = "SELECT * FROM volunteer" 
    rows = execute_read_query(conn,query)
    return jsonify(rows)

@app.route('/add_volunteer', methods =['POST']) # API allows user to add a new volunteer to the database: http://127.0.0.1:5000/add_volunteer
def add_volunteer():
    request_data = request.get_json() # stores json input into variables
    first_name = request_data['first_name']
    last_name = request_data['last_name']
    phone = request_data['phone']
    email = request_data['email']
    emergency_contact_fname = request_data['emergency_contact_fname']
    emergency_contact_lname = request_data['emergency_contact_lname']
    emergency_contact_phone = request_data['emergency_contact_phone']
    address_line_1 = request_data['address_line_1']
    address_line_2 = request_data['address_line_2']
    city = request_data['city']
    state_id = request_data['state_id']
    date_created = request_data['date_created']
    volunteer_status_id = request_data['volunteer_status_id']
    rel_status_id = request_data['rel_status_id']
    waiver_signed = request_data['waiver_signed']
    date_waived_signed = request_data['date_waived_signed']

    
    ### query for inserting data ###
    query = "INSERT INTO volunteer (first_name, last_name, phone, email, emergency_contact_fname, emergency_contact_lname, emergency_contact_phone) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" \
        % (first_name, last_name, phone, email, emergency_contact_fname, emergency_contact_lname, emergency_contact_phone) # inserts new entry in volunteer table
   
    execute_query(conn, query)

    return "Add request successful"

if __name__ == "__main__":
    app.run()