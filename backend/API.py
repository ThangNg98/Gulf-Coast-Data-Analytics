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

@app.route('/update_volunteer', methods =['POST']) # API allows user to update an volunteer to the database: http://127.0.0.1:5000/update_volunteer
def update_volunteer():
    request_data = request.get_json() # stores json input into variables
    new_id = request_data['id']
    new_first_name = request_data['first_name']
    new_last_name = request_data['last_name']
    new_phone = request_data['phone']
    new_email = request_data['email']
    new_emer_con_fname = request_data['emergency_contact_fname']
    new_emer_con_lname = request_data['emergency_contact_lname']
    new_emer_con_phone = request_data['emergency_contact_phone']
    new_add_1 = request_data['address_line_1']
    new_add_2 = request_data['address_line_2']
    new_city = request_data['city']
    new_state = request_data['state_id']
    new_zip = request_data['zip']
    new_rel_id = request_data['rel_id']

    ### query for updating data ###
    query = "UPDATE volunteer SET first_name='%s', last_name='%s', phone='%s', email='%s', emergency_contact_fname='%s',  emergency_contact_lname='%s',  emergency_contact_phone='%s',  address_line_1='%s',  address_line_2='%s',  city='%s',  state_id='%s', zip='%s', rel_id=%s WHERE id=%s"%(new_first_name, new_last_name, new_phone,new_email,new_emer_con_fname,new_emer_con_lname, new_emer_con_phone, new_add_1, new_add_2, new_city, new_state,new_zip, new_rel_id, new_id)
   
    execute_query(conn, query)

    return "Update request successful"

@app.route('/admin_update_volunteer', methods =['POST']) # API allows user to update an volunteer to the database: http://127.0.0.1:5000/admin_update_volunteer
def admin_update_volunteer():
    request_data = request.get_json() # stores json input into variables
    new_id = request_data['id']
    new_first_name = request_data['first_name']
    new_last_name = request_data['last_name']
    new_phone = request_data['phone']
    new_email = request_data['email']
    new_emer_con_fname = request_data['emergency_contact_fname']
    new_emer_con_lname = request_data['emergency_contact_lname']
    new_emer_con_phone = request_data['emergency_contact_phone']
    new_add_1 = request_data['address_line_1']
    new_add_2 = request_data['address_line_2']
    new_city = request_data['city']
    new_state = request_data['state_id']
    new_zip = request_data['zip']
    new_rel_id = request_data['rel_id']
    new_waiver_signed = request_data['waiver_signed']
    new_date_waiver_signed = request_data['date_waiver_signed'] 

    ### query for updating data ###
    query = "UPDATE volunteer SET first_name='%s', last_name='%s', phone='%s', email='%s', emergency_contact_fname='%s',  emergency_contact_lname='%s',  emergency_contact_phone='%s',  address_line_1='%s',  address_line_2='%s',  city='%s',  state_id='%s', zip='%s', rel_id=%s, waiver_signed=%s, date_waiver_signed=STR_TO_DATE('%s', '%%Y-%%m-%%d') WHERE id=%s"%(new_first_name, new_last_name, new_phone,new_email,new_emer_con_fname,new_emer_con_lname, new_emer_con_phone, new_add_1, new_add_2, new_city, new_state,new_zip, new_rel_id, new_waiver_signed, new_date_waiver_signed,new_id)
   
    execute_query(conn, query)

    return "Update request successful"

@app.route('/delete_volunteer', methods =['POST']) # API allows user to set the volunteer status to inactive in the database: http://127.0.0.1:5000/delete_volunteer
def delete_volunteer():
    request_data = request.get_json() # stores json input into variables
    id = request_data['id']
    new_status_id = 2 

    ### query for updating data ###
    query = "UPDATE volunteer SET volunteer_status_id=%s WHERE id=%s"%(new_status_id,id)
   
    execute_query(conn, query)

    return "Delete request successful"

if __name__ == "__main__":
    app.run()