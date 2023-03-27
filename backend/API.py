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

##### returns all the volunteers in the volunteers table ######
@app.route('/', methods = ['GET']) # http://127.0.0.1:5000/
def home():
    
    query = "SELECT volunteers.first_name, volunteers.last_name, volunteers.phone, volunteers.email, volunteers.emergency_contact_fname, emergency_contact_lname, emergency_contact_phone FROM volunteers" 
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

    
    ### query for inserting data ###
    query = "INSERT INTO volunteers (first_name, last_name, phone, email, emergency_contact_fname, emergency_contact_lname, emergency_contact_phone) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" \
        % (first_name, last_name, phone, email, emergency_contact_fname, emergency_contact_lname, emergency_contact_phone) # inserts new entry in volunteers table
   
    execute_query(conn, query)

    return "Add request successful"

@app.route('/create_session', methods = ['POST']) # http://127.0.0.1:5000/
def create_session():
    request_data = request.get_json() # stores json input into variables
    time_in = request_data['time_in']
    time_out = request_data['time_out']
    session_date = request_data['session_date']
    session_comment = request_data['session_comment']
    org_id = request_data['org_id']
    event_id = request_data['event_id']
    session_staus_id = request_data['session_staus_id']
    
    query = "INSERT INTO session (time_in, time_out, session_date, session_comment, org_id, event_id, session_staus_id) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s');" \
        % (time_in, time_out, session_date, session_comment, org_id, event_id, session_staus_id)
    execute_query(conn,query)
    return "Add session request successful"


if __name__ == "__main__":
    app.run()