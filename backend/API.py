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

############## SESSIONS ##################
@app.route('/create_session', methods = ['POST']) # http://127.0.0.1:5000/
def create_session():
    request_data = request.get_json() # stores json input into variables
    time_in = request_data['time_in']
    session_date = request_data['session_date']
    session_comment = request_data['session_comment']
    org_id = request_data['org_id']
    event_id = request_data['event_id']
    session_status_id = request_data['session_status_id']
    volunteer_id = request_data['volunteer_id']
    
    query = "INSERT INTO session (time_in, session_date, session_comment, org_id, event_id, session_status_id, volunteer_id) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s');" \
        % (time_in, session_date, session_comment, org_id, event_id, session_status_id, volunteer_id)
    execute_query(conn,query)
    
    
    return "Add session request successful"

@app.route('/check_out', methods = ['POST']) # http://127.0.0.1:5000/check_out
def check_out():
    request_data = request.get_json() # stores json input into variables
    print('request_data:', request_data)
    session_id = request_data['session_id']
    new_time_out = request_data['time_out']
    
    query = "UPDATE session SET time_out='%s'WHERE session_id=%s"%(new_time_out, session_id)
    execute_query(conn,query)
    return "Add check out time request successful"


############# EVENTS ###############

@app.route('/create_event', methods=['POST'])
def create_event():
    request_data = request.get_json() # stores json input into variables
    event_name = request_data['event_name']
    event_description = request_data['event_description']

    query = "INSERT INTO event (event_name,event_description, event_status_id) values ('%s', '%s', '1')" \
        % (event_name, event_description) # inserts new entry in event table

    execute_query(conn, query)

    return "Add event successful"

# this api will get an event by id
@app.route('/get_event/<event_id>', methods = ['GET']) # http://127.0.0.1:5000/get_event/1
def get_event(event_id): # returns all the events in the events table that have active status "1"
    query = "select event.event_id, event.event_name, event.event_description, sum(session.total_hours) as total_hours, \
            count(session.volunteer_id) as num_volunteers from event \
            LEFT JOIN session on event.event_id=session.event_id WHERE event.event_id='%s'" % event_id
    rows = execute_read_query(conn,query)   
    return jsonify(rows)


@app.route('/read_events', methods = ['GET']) # http://127.0.0.1:5000/read_events
def read_events(): # returns all the events in the events table that have active status "1"
    
    query = "SELECT * FROM event WHERE event.event_status_id = 1" 
    rows = execute_read_query(conn,query)
    return jsonify(rows)


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

############# ORGANIZATIONS ###############

@app.route('/create_organization', methods =['POST']) # API allows user to create an organization: http://127.0.0.1:5000/create_organization
def create_organization():
    request_data = request.get_json() # stores json input into variables
    org_name = request_data['org_name']
    address_line_1 = request_data['address_line_1']
    address_line_2 = request_data['address_line_2']
    city = request_data['city']
    state_id = request_data['state_id']
    zip = request_data['zip']
    
    query = "INSERT INTO organization (org_name, address_line_1, address_line_2, city, state_id, zip, org_status_id) values ('%s', '%s', '%s', '%s', '%s', '%s', '1')" \
        % (org_name, address_line_1, address_line_2, city, state_id, zip)
        
    execute_query(conn, query)
    
    return "Create Organization Request Successful"
    
# this api will get an org by id
@app.route('/get_org/<org_id>', methods = ['GET']) # http://127.0.0.1:5000/get_org/1
def get_org(org_id): # returns all the orgs in the organizations table that have active status "1"
    query = "select organization.org_id, organization.org_name, organization.address_line_1, \
            organization.address_line_2, organization.city, organization.state_id, \
            organization.zip, organization.org_status_id, sum(session.total_hours) as total_hours, \
            count(session.volunteer_id) as num_volunteers from organization \
            LEFT JOIN session on organization.org_id=session.org_id WHERE organization.org_id='%s'" % org_id
    rows = execute_read_query(conn,query)
    return jsonify(rows)


@app.route('/read_orgs', methods = ['GET']) # http://127.0.0.1:5000/read_orgs
def read_orgs():
    
    query = "SELECT * FROM organization WHERE org_status_id = 1" # query for selecting all active orgs
    rows = execute_read_query(conn,query)
    return jsonify(rows)

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


############# VOLUNTEERS ###############

@app.route('/read_volunteers', methods = ['GET']) # http://127.0.0.1:5000/read_volunteers
def read_volunteers():

    query = "SELECT * FROM volunteer WHERE volunteer_status_id = 1" ### CHANGE ME THIS 2 IS FOR TESTING ###
    rows = execute_read_query(conn,query)
    return jsonify(rows)

@app.route('/update_volunteer', methods =['POST']) # API allows user to update an volunteer to the database: http://127.0.0.1:5000/update_volunteer
def update_volunteer():
    request_data = request.get_json() # stores json input into variables
    new_id = request_data['volunteer_id']
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
    query = "UPDATE volunteer SET first_name='%s', last_name='%s', phone='%s', email='%s', emergency_contact_fname='%s',  emergency_contact_lname='%s',  emergency_contact_phone='%s',  address_line_1='%s',  address_line_2='%s',  city='%s',  state_id='%s', zip='%s', rel_id=%s WHERE volunteer_id=%s"%(new_first_name, new_last_name, new_phone,new_email,new_emer_con_fname,new_emer_con_lname, new_emer_con_phone, new_add_1, new_add_2, new_city, new_state,new_zip, new_rel_id, new_id)

    execute_query(conn, query)

    return "Update request successful"

@app.route('/admin_update_volunteer', methods =['POST']) # API allows user to update an volunteer to the database: http://127.0.0.1:5000/admin_update_volunteer
def admin_update_volunteer():
    request_data = request.get_json() # stores json input into variables
    new_id = request_data['volunteer_id']
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

    if (request_data['date_waiver_signed'] == None): #if date_waiver_signed = null
        query = "UPDATE volunteer SET first_name='%s', last_name='%s', phone='%s', email='%s', emergency_contact_fname='%s',  emergency_contact_lname='%s',  emergency_contact_phone='%s',  address_line_1='%s',  address_line_2='%s',  city='%s',  state_id='%s', zip='%s', rel_id=%s, waiver_signed=%s WHERE volunteer_id=%s"%(new_first_name, new_last_name, new_phone,new_email,new_emer_con_fname,new_emer_con_lname, new_emer_con_phone, new_add_1, new_add_2, new_city, new_state,new_zip, new_rel_id, new_waiver_signed, new_id)

    else: #if there is a new date waiver signed
        ### query for updating data ###
        query = "UPDATE volunteer SET first_name='%s', last_name='%s', phone='%s', email='%s', emergency_contact_fname='%s',  emergency_contact_lname='%s',  emergency_contact_phone='%s',  address_line_1='%s',  address_line_2='%s',  city='%s',  state_id='%s', zip='%s', rel_id=%s, waiver_signed=%s, date_waiver_signed=STR_TO_DATE('%s', '%%Y-%%m-%%d') WHERE volunteer_id=%s"%(new_first_name, new_last_name, new_phone,new_email,new_emer_con_fname,new_emer_con_lname, new_emer_con_phone, new_add_1, new_add_2, new_city, new_state,new_zip, new_rel_id, new_waiver_signed, new_date_waiver_signed,new_id)

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

# this api will get an volunteer by id
@app.route('/get_volunteer/<volunteer_id>', methods = ['GET']) # http://127.0.0.1:5000/get_volunteer/1
def get_volunteer(volunteer_id): 
    query = "SELECT * FROM volunteer WHERE volunteer.volunteer_id = %s" % volunteer_id
    rows = execute_read_query(conn,query)
    return jsonify(rows)    

@app.route('/volunteer_phone/', methods = ['GET'])
def volunteer_phone():
    query = """
        SELECT phone
        FROM volunteer
    """
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
    volunteer_status_id = 1
    rel_id = request_data['rel_id']
    waiver_signed = 2
    zip = request_data['zip']

    # Check if phone value is not already in the volunteer table
    query = "SELECT * FROM volunteer WHERE phone = '%s' AND volunteer_status_id = 1" % (phone)
    result = execute_read_query(conn, query)
    if result:
        print('Volunteer with this phone number already exists.')
        return '1'
    else:
        print('Volunteer with this phone number does not exist. New volunteer added.')
        # If phone number is not in the volunteer table, insert new entry
        query = "INSERT INTO volunteer (first_name, last_name, phone, email, emergency_contact_fname, emergency_contact_lname, emergency_contact_phone, address_line_1, address_line_2, city, state_id, date_created, volunteer_status_id, rel_id, waiver_signed, zip) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" \
            % (first_name, last_name, phone, email, emergency_contact_fname, emergency_contact_lname, emergency_contact_phone, address_line_1, address_line_2, city, state_id, date_created, volunteer_status_id, rel_id, waiver_signed, zip) # inserts new entry in volunteer table
    
        execute_query(conn, query)

        return '2'
if __name__ == "__main__":
    app.run()