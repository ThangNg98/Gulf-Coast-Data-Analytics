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

@app.route('/update_event', methods =['POST']) # API allows user to update an event to the database: http://127.0.0.1:5000/update_event
def update_event():
    request_data = request.get_json() # stores json input into variables
    event_id = request_data['event_id']
    new_name = request_data['event_name']
    new_description = request_data['event_description']

    ### query for updating data ###
    query = "UPDATE event SET event_name='%s', event_description='%s' WHERE event_id=%s"%(new_name,new_description,event_id)
   
    execute_query(conn, query)

    return "Update request successful"

@app.route('/delete_event', methods =['POST']) # API allows user to update an event to the database: http://127.0.0.1:5000/delete_event
def delete_event():
    request_data = request.get_json() # stores json input into variables
    event_id = request_data['event_id']
    new_status_id = 2 

    ### query for updating data ###
    query = "UPDATE event SET event_status_id=%s WHERE event_id=%s"%(new_status_id,event_id)
   
    execute_query(conn, query)

    return "Delete request successful"

@app.route('/update_organization', methods =['POST']) # API allows user to update an organization to the database: http://127.0.0.1:5000/update_organization
def update_organization():
    request_data = request.get_json() # stores json input into variables
    org_id = request_data['org_id']
    new_name = request_data['org_name']
    new_address_1 = request_data['address_line_1']
    new_address_2 = request_data['address_line_2']
    new_city = request_data['city']
    new_state_id = request_data['state_id']
    new_zip = request_data['zip']

    ### query for updating data ###
    query = "UPDATE organization SET org_name='%s', address_line_1='%s', address_line_2='%s',city='%s',state_id=%s,zip=%s WHERE org_id=%s"%(new_name,new_address_1,new_address_2,new_city,new_state_id,new_zip,org_id)

    execute_query(conn, query)

    return "Update request successful"

@app.route('/delete_organization', methods =['POST']) # API allows user to delete an organization to the database: http://127.0.0.1:5000/delete_organization
def delete_organization():
    request_data = request.get_json() # stores json input into variables
    org_id = request_data['org_id']
    new_status_id = 2 

    ### query for updating data ###
    query = "UPDATE organization SET org_status_id=%s WHERE org_id=%s"%(new_status_id,org_id)

    execute_query(conn, query)

    return "Delete request successful"
    
if __name__ == "__main__":
    app.run()