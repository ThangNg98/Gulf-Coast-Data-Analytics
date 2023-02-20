import flask
import hashlib
from flask import request, make_response, jsonify
import mysql.connector
from mysql.connector import Error
from sql import create_connection, execute_query, execute_read_query
from datetime import datetime

conn = create_connection('172.26.54.22', 'ADMIN', 'password123!', 'llc_database') # connection to database

# setup application
app = flask.Flask(__name__)
app.config["DEBUG"] = True

##### returns all the volunteers in the volunteers table ######
@app.route('/', methods = ['GET']) # http://127.0.0.1:5000/api/
def home():
    
    query = "SELECT volunteers.first_name, volunteers.last_name, volunteers.phone FROM volunteers" 
    rows = execute_read_query(conn,query)
    return jsonify(rows)

@app.route('/add_volunteer', methods =['POST']) # API allows user to add a new volunteer to the database: http://127.0.0.1:5000/api/add_volunteer
def add_volunteer():
    request_data = request.get_json() # stores json input into variables
    first_name = request_data['first_name']
    last_name = request_data['last_name']
    phone_number = request_data['phone_number']

    
    ### user can select an existing destination from the destination table ###
    query = "INSERT INTO volunteers (first_name, last_name, phone) VALUES ('%s', '%s', '%s')" \
        % (first_name, last_name, phone_number) # inserts new entry in trip table
   
    execute_query(conn, query)

    return "Add request successful"

if __name__ == "__main__":
    app.run()