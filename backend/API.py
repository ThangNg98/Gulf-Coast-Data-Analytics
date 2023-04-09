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
@app.route('/check_most_recent/<volunteer_id>', methods=['GET'])
def check_most_recent(volunteer_id):
    print('volunteer_id:', volunteer_id)
    query = """
        WITH most_recent AS (
            SELECT MAX(session_id) AS max_session_id
            FROM (
                SELECT session_id, time_in 
                FROM session
                WHERE volunteer_id = '%s'
                AND session_status_id = 1
            ) AS recent_sessions
        )
        SELECT 
            session_id, 
            TIME_FORMAT(time_in, '%%h:%%i %%p') AS time_in,
            IF(time_out IS NULL, '1', '2') AS time_out,
            org_id,
            event_id,
            session_comment
        FROM session
        WHERE session_id = (
            SELECT max_session_id
            FROM most_recent
        );
    """ % volunteer_id
    rows = execute_read_query(conn, query)
    print('rows:', rows)
    return jsonify(rows)



@app.route('/create_session', methods = ['POST'])
def create_session():
    request_data = request.get_json()
    print('request_data create session', request_data)
    time_in = request_data['time_in']
    session_date = request_data['session_date']
    session_comment = request_data['session_comment']
    org_id = request_data['org_id']
    event_id = request_data['event_id']
    session_status_id = request_data['session_status_id']
    volunteer_id = request_data['volunteer_id']

    if (org_id == None or session_comment == None):
        query = """
            INSERT INTO session (
                time_in,
                session_date,
                session_comment,
                event_id,
                session_status_id,
                volunteer_id
            )
            VALUES (
                %s, %s, %s, %s, %s, %s
            );
        """
        params = (time_in, session_date, session_comment, event_id, session_status_id, volunteer_id)
    
    else:
        query = "INSERT INTO session (time_in, session_date, session_comment, org_id, event_id, session_status_id, volunteer_id) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        params = (time_in, session_date, session_comment, org_id, event_id, session_status_id, volunteer_id)
    
    execute_query(conn, query, params)
    event_name = "event" + str(time_in).replace(":", "")
    
    query_auto_logout = "CREATE EVENT " + event_name + " ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 8 HOUR DO UPDATE session SET time_out = NOW() where time_in = %s && time_out is null;"
    params = (time_in,)
    execute_query(conn, query_auto_logout, params)

    
    return "Add session request successful"


@app.route('/check_out', methods = ['POST'])
def check_out():
    request_data = request.get_json()
    print('request_data:', request_data)
    session_id = request_data['session_id']
    new_time_out = request_data['time_out']

    query = "UPDATE session SET time_out=%s WHERE session_id=%s"
    params = (new_time_out, session_id)
    execute_query(conn, query, params)

    return "Add check out time request successful"


@app.route('/read_sessions', methods = ['GET']) # http://127.0.0.1:5000/read_sessions
#API to get Open Sessions
def read_sessions():

    query = """ SELECT session.session_id, CONCAT(volunteer.first_name, ' ', volunteer.last_name) AS volunteer_name,
            DATE_FORMAT(session.session_date, '%m/%d/%Y') AS session_date,
            event.event_name,
            organization.org_name,
            DATE_FORMAT(session.time_in, '%h:%i %p') AS time_in,
            DATE_FORMAT(session.time_out, '%h:%i %p') AS time_out,
            session_comment,
            volunteer.phone
            FROM session
            JOIN volunteer ON session.volunteer_id = volunteer.volunteer_id
            JOIN event ON session.event_id = event.event_id
            LEFT OUTER JOIN organization ON session.org_id = organization.org_id
            JOIN session_status ON session.session_status_id = session_status.session_status_id
            WHERE session.session_status_id = 1 AND session.time_out IS NULL
             """ 
    rows = execute_read_query(conn,query)
    return jsonify(rows)

@app.route('/read_closed_sessions', methods = ['GET']) # http://127.0.0.1:5000/read_closed_sessions
#API to get Open Sessions
def read_closed_sessions():

    query = """ SELECT session.session_id, CONCAT(volunteer.first_name, ' ', volunteer.last_name) AS volunteer_name,
            DATE_FORMAT(session.session_date, '%m/%d/%Y') AS session_date,
            event.event_name,
            organization.org_name,
            DATE_FORMAT(session.time_in, '%h:%i %p') AS time_in,
            DATE_FORMAT(session.time_out, '%h:%i %p') AS time_out,
            session_comment,
            total_hours,
            volunteer.phone
            FROM session
            JOIN volunteer ON session.volunteer_id = volunteer.volunteer_id
            JOIN event ON session.event_id = event.event_id
            LEFT OUTER JOIN organization ON session.org_id = organization.org_id
            JOIN session_status ON session.session_status_id = session_status.session_status_id
            WHERE session.session_status_id = 1 AND session.time_out IS NOT NULL
             """ 
    rows = execute_read_query(conn,query)
    return jsonify(rows)    
        # Helmut = gets all sessions
        # Sends us ID
        # In update page, we use ID to get info to fill fields

        #Helmut send us everything
@app.route('/read_session/<session_id>', methods = ['GET'])
def read_session(session_id):
    query = """
        SELECT 
            s.session_id, 
            TIME_FORMAT(s.time_in, '%%H:%%i') AS time_in, 
            TIME_FORMAT(s.time_out, '%%H:%%i') AS time_out, 
            DATE_FORMAT(s.session_date, '%%Y-%%m-%%d') AS session_date,
            s.session_comment,
            CONCAT(v.first_name, ' ', v.last_name) AS full_name,
            s.org_id,
            s.event_id
        FROM session s
        JOIN volunteer v ON s.volunteer_id = v.volunteer_id
        WHERE s.session_id = %s;
    """ % session_id
    rows = execute_read_query(conn,query)
    print('LORI', rows)
    return jsonify(rows)   

@app.route('/current_session/<session_id>', methods = ['GET'])
def current_session(session_id):   
    query = """
        SELECT org_name, event_name, TIME_FORMAT(time_in, '%%h:%%i %%p') AS time_in
        FROM session
        JOIN event ON session.event_id = event.event_id
        JOIN organization ON session.org_id = organization.org_id
        WHERE session_id = %s;        
    
    
    """ % session_id
    rows = execute_read_query(conn,query)
    print(rows)
    return jsonify(rows)

@app.route('/update_session', methods=['POST'])
def update_session():
    request_data = request.get_json() # stores json input into variables
    session_id = request_data['session_id']
    new_time_in = request_data['time_in']
    new_time_out = request_data['time_out']
    new_session_date = request_data['session_date']
    new_session_comment = request_data['session_comment']
    new_org_id = request_data['org_id']
    new_event_id = request_data['event_id']

    if new_org_id is None or new_time_out is None:
        if new_org_id is None and new_time_out is not None: # if org_id is null
            query = "UPDATE session SET time_in=%s, time_out=%s, session_date=%s, session_comment=%s, org_id=NULL, event_id=%s WHERE session_id=%s"
            params = (new_time_in, new_time_out, new_session_date, new_session_comment, new_event_id, session_id)
        elif new_org_id is None and new_time_out is None:
            query = "UPDATE session SET time_in=%s, time_out=NULL, session_date=%s, session_comment=%s, org_id=NULL, event_id=%s WHERE session_id=%s"
            params = (new_time_in, new_session_date, new_session_comment, new_event_id, session_id)
        elif new_org_id is not None and new_time_out is None:
            query = "UPDATE session SET time_in=%s, time_out=NULL, session_date=%s, session_comment=%s, org_id=%s, event_id=%s WHERE session_id=%s"
            params = (new_time_in, new_session_date, new_session_comment, new_org_id, new_event_id, session_id)
    else:
        query = "UPDATE session SET time_in=%s, time_out=%s, session_date=%s, session_comment=%s, org_id=%s, event_id=%s WHERE session_id=%s"
        params = (new_time_in, new_time_out, new_session_date, new_session_comment, new_org_id, new_event_id, session_id)

    execute_query(conn, query, params)

    return "Update request successful"




@app.route('/delete_session', methods=['POST'])
def delete_session():
    request_data = request.get_json()
    session_id = request_data['session_id']
    new_status_id = 2
    query = "UPDATE session SET session_status_id=%s WHERE session_id=%s"
    params = (new_status_id, session_id)
    execute_query(conn, query, params)
    return "Delete request successful"


############# EVENTS ###############

@app.route('/create_event', methods=['POST'])
def create_event():
    request_data = request.get_json()
    event_name = request_data['event_name']
    event_description = request_data['event_description']

    query = "INSERT INTO event (event_name, event_description, event_status_id) values (%s, %s, '1')"
    params = (event_name, event_description)

    execute_query(conn, query, params)

    return "Add event successful"


# this api will get an event by id
@app.route('/get_event/<event_id>', methods = ['GET']) # http://127.0.0.1:5000/get_event/1
def get_event(event_id): # returns all the events in the events table that have active status "1"
    query = "select event.event_id, event.event_name, event.event_description, sum(session.total_hours) as total_hours, \
            count(distinct session.volunteer_id) as num_volunteers from event \
            LEFT JOIN session on event.event_id=session.event_id WHERE event.event_id='%s'" % event_id
    rows = execute_read_query(conn,query)   
    return jsonify(rows)


@app.route('/read_events', methods = ['GET']) # http://127.0.0.1:5000/read_events
def read_events(): # returns all the events in the events table that have active status "1"
    
    query = "SELECT * FROM event WHERE event.event_status_id = 1 ORDER BY event_name" 
    rows = execute_read_query(conn,query)
    return jsonify(rows)


@app.route('/update_event', methods =['POST'])
def update_event():
    request_data = request.get_json()
    event_id = request_data['event_id']
    new_name = request_data['event_name']
    new_description = request_data['event_description']

    query = "UPDATE event SET event_name=%s, event_description=%s WHERE event_id=%s"
    params = (new_name, new_description, event_id)

    execute_query(conn, query, params)

    return "Update request successful"


@app.route('/delete_event', methods =['POST'])
def delete_event():
    request_data = request.get_json()
    event_id = request_data['event_id']
    new_status_id = 2 

    query = "UPDATE event SET event_status_id=%s WHERE event_id=%s"
    params = (new_status_id, event_id)

    execute_query(conn, query, params)

    return "Delete request successful"


############# ORGANIZATIONS ###############

@app.route('/create_organization', methods =['POST'])
def create_organization():
    request_data = request.get_json()
    org_name = request_data['org_name']
    address_line_1 = request_data['address_line_1']
    address_line_2 = request_data['address_line_2']
    city = request_data['city']
    state_id = request_data['state_id']
    zip = request_data['zip']

    query = "INSERT INTO organization (org_name, address_line_1, address_line_2, city, state_id, zip, org_status_id) values (%s, %s, %s, %s, %s, %s, '1')"
    params = (org_name, address_line_1, address_line_2, city, state_id, zip)

    execute_query(conn, query, params)

    return "Create Organization Request Successful"

    
# this api will get an org by id
@app.route('/get_org/<org_id>', methods = ['GET']) # http://127.0.0.1:5000/get_org/1
def get_org(org_id): # returns all the orgs in the organizations table that have active status "1"
    query = "select organization.org_id, organization.org_name, organization.address_line_1, \
            organization.address_line_2, organization.city, organization.state_id, \
            organization.zip, organization.org_status_id, sum(session.total_hours) as total_hours, \
            count(distinct session.volunteer_id) as num_volunteers from organization \
            LEFT JOIN session on organization.org_id=session.org_id WHERE organization.org_id='%s'" % org_id
    rows = execute_read_query(conn,query)
    return jsonify(rows)


@app.route('/read_orgs', methods = ['GET']) # http://127.0.0.1:5000/read_orgs
def read_orgs():
    
    query = "SELECT * FROM organization WHERE org_status_id = 1 ORDER BY org_name" # query for selecting all active orgs
    rows = execute_read_query(conn,query)
    return jsonify(rows)

@app.route('/update_organization', methods =['POST'])
def update_organization():
    request_data = request.get_json()
    org_id = request_data['org_id']
    new_name = request_data['org_name']
    new_address_1 = request_data['address_line_1']
    new_address_2 = request_data['address_line_2']
    new_city = request_data['city']
    new_state_id = request_data['state_id']
    new_zip = request_data['zip']

    query = "UPDATE organization SET org_name=%s, address_line_1=%s, address_line_2=%s, city=%s, state_id=%s, zip=%s WHERE org_id=%s"
    params = (new_name, new_address_1, new_address_2, new_city, new_state_id, new_zip, org_id)

    execute_query(conn, query, params)

    return "Update request successful"


@app.route('/delete_organization', methods =['POST'])
def delete_organization():
    request_data = request.get_json()
    org_id = request_data['org_id']
    new_status_id = 2 

    query = "UPDATE organization SET org_status_id=%s WHERE org_id=%s"
    params = (new_status_id, org_id)

    execute_query(conn, query, params)

    return "Delete request successful"



############# VOLUNTEERS ###############

@app.route('/read_volunteers', methods = ['GET']) # http://127.0.0.1:5000/read_volunteers
def read_volunteers():

    # This query needs to join the volunteer table with the session table by volunteer_id and sum the total hours for each volunteer 
    query = """SELECT volunteer.volunteer_id, volunteer.first_name, volunteer.last_name, volunteer.phone, volunteer.email, volunteer.emergency_contact_fname, 
    volunteer.emergency_contact_lname, volunteer.emergency_contact_phone, volunteer.address_line_1, volunteer.address_line_2, volunteer.city, volunteer.volunteer_status_id, 
    volunteer.date_created, volunteer.volunteer_status_id, volunteer.rel_id, volunteer.waiver_signed, volunteer.date_waiver_signed, volunteer.zip,
    sum(session.total_hours) as total_hours 
    FROM volunteer 
    LEFT JOIN session 
    ON volunteer.volunteer_id=session.volunteer_id 
    WHERE volunteer.volunteer_status_id = 1 
    GROUP BY volunteer.volunteer_id
    ORDER BY first_name"""
    rows = execute_read_query(conn,query)
    return jsonify(rows)

@app.route('/read_volunteer_hours/<volunteer_id>', methods = ['GET']) # http://127.0.0.1:5000/read_volunteer_hours
def read_volunteers_hours(volunteer_id):   
    query = """select sum(session.total_hours) as total_hours
                from session
                where volunteer_id = %s """ % volunteer_id

    rows = execute_read_query(conn,query)
    return jsonify(rows)
    


@app.route('/update_volunteer', methods =['POST'])
def update_volunteer():
    request_data = request.get_json()
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

    query = "UPDATE volunteer SET first_name=%s, last_name=%s, phone=%s, email=%s, emergency_contact_fname=%s, emergency_contact_lname=%s, emergency_contact_phone=%s, address_line_1=%s, address_line_2=%s, city=%s, state_id=%s, zip=%s, rel_id=%s WHERE volunteer_id=%s"
    params = (new_first_name, new_last_name, new_phone, new_email, new_emer_con_fname, new_emer_con_lname, new_emer_con_phone, new_add_1, new_add_2, new_city, new_state, new_zip, new_rel_id, new_id)

    execute_query(conn, query, params)

    return "Update request successful"


@app.route('/admin_update_volunteer', methods=['POST'])
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
    
    if new_date_waiver_signed is None:
        query = """
            UPDATE volunteer SET 
                first_name=%s, 
                last_name=%s, 
                phone=%s, 
                email=%s, 
                emergency_contact_fname=%s,  
                emergency_contact_lname=%s,  
                emergency_contact_phone=%s,  
                address_line_1=%s,  
                address_line_2=%s,  
                city=%s,  
                state_id=%s, 
                zip=%s, 
                rel_id=%s, 
                waiver_signed=%s 
            WHERE volunteer_id=%s
        """
        params = (
            new_first_name, 
            new_last_name, 
            new_phone, 
            new_email, 
            new_emer_con_fname, 
            new_emer_con_lname, 
            new_emer_con_phone, 
            new_add_1, 
            new_add_2, 
            new_city, 
            new_state, 
            new_zip, 
            new_rel_id, 
            new_waiver_signed, 
            new_id
        )
    else:
        query = """
            UPDATE volunteer SET 
                first_name=%s, 
                last_name=%s, 
                phone=%s, 
                email=%s, 
                emergency_contact_fname=%s,  
                emergency_contact_lname=%s,  
                emergency_contact_phone=%s,  
                address_line_1=%s,  
                address_line_2=%s,  
                city=%s,  
                state_id=%s, 
                zip=%s, 
                rel_id=%s, 
                waiver_signed=%s, 
                date_waiver_signed=STR_TO_DATE(%s, '%%Y-%%m-%%d') 
            WHERE volunteer_id=%s
        """
        params = (
            new_first_name, 
            new_last_name, 
            new_phone, 
            new_email, 
            new_emer_con_fname, 
            new_emer_con_lname, 
            new_emer_con_phone, 
            new_add_1, 
            new_add_2, 
            new_city, 
            new_state, 
            new_zip, 
            new_rel_id, 
            new_waiver_signed, 
            new_date_waiver_signed, 
            new_id
        )

    execute_query(conn, query, params)

    return "Update request successful"


@app.route('/delete_volunteer', methods=['POST'])
def delete_volunteer():
    request_data = request.get_json()
    volunteer_id = request_data['volunteer_id']
    new_status_id = 2

    query = "UPDATE volunteer SET volunteer_status_id=%s WHERE volunteer_id=%s"
    params = (new_status_id, volunteer_id)
    
    execute_query(conn, query, params)

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
        SELECT volunteer_id, phone, first_name, waiver_signed
        FROM volunteer
        WHERE volunteer_status_id = 1
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

@app.route('/get_volunteer_id/<volunteer_phone>', methods=['GET'])
def get_volunteer_id(volunteer_phone):
    print('volunteer_phone:', volunteer_phone)
    query = """
        SELECT volunteer_id, first_name
        FROM volunteer
        WHERE phone = '%s'
        AND volunteer_status_id = 1
    """ % volunteer_phone
    rows = execute_read_query(conn, query)
    print(rows)
    return jsonify(rows)

############# ADMIN DASHBOARD #############
@app.route('/get_hist_6', methods=['GET'])
def get_full_history():
    query = """
        SELECT DATE_FORMAT(session.session_date, '%M') as MonthName, YEAR(session.session_date) as YearName,
        SUM(session.total_hours) as TotalHours, COUNT(DISTINCT session.volunteer_id) as UniqueVolunteers,
        COUNT(session.volunteer_id) as TotalVolunteers, DATE_FORMAT(session.session_date, '%m') as MonthNum
        from session
        JOIN volunteer ON session.volunteer_id=volunteer.volunteer_id
        WHERE session_date >= DATE_SUB(NOW(), INTERVAL 5 MONTH)  AND session_date <= NOW() and volunteer.volunteer_status_id = 1
        GROUP BY MonthName, MonthNum, YEAR(session_date)
        ORDER BY YEAR(session_date) DESC, MonthNum DESC;
    """
    rows = execute_read_query(conn, query)
    return jsonify(rows)

#hours per org last 6 months
@app.route('/get_orgs_6', methods=['GET'])
def get_orgs_6():
    query = """
        select organization.org_name as orgNames, SUM(session.total_hours) as orgHours from session
        left join organization
        on session.org_id = organization.org_id
        WHERE session_date >= DATE_SUB(NOW(), INTERVAL 5 MONTH)  AND session_date <= NOW()
        GROUP BY orgNames
        ORDER BY orgNames;
    """
    rows = execute_read_query(conn, query)
    return jsonify(rows)

# Admin Reports
@app.route('/getOrgsHours', methods=['GET'])
def getOrgsHours():
    query = """
        SELECT s.org_id, o.org_name, SUM(s.total_hours) AS total_hours_per_org
        FROM session s
        JOIN organization o
        ON s.org_id = o.org_id
        WHERE o.org_status_id = 1
        GROUP BY org_id;
    """
    rows = execute_read_query(conn, query)
    return jsonify(rows)

@app.route('/getOrgsVolunteers', methods=['GET'])
def getOrgsVolunteers():
        query = """
            SELECT s.org_id, o.org_name, COUNT(s.volunteer_id) as num_volunteers
            FROM session s
            JOIN organization o
            ON s.org_id = o.org_id
            JOIN volunteer v
            ON s.volunteer_id = v.volunteer_id
            WHERE o.org_status_id = 1
            AND v.volunteer_status_id = 1
            GROUP BY s.org_id;
        """
        rows = execute_read_query(conn, query)
        return jsonify(rows)

@app.route('/getOrgsHoursVolunteers', methods=['GET'])
def getOrgsHoursVolunteers():
    query = """
        SELECT s.org_id, o.org_name, SUM(s.total_hours) AS total_hours_per_org, COUNT(s.volunteer_id) as num_volunteers
        FROM session s
        JOIN organization o
        ON s.org_id = o.org_id
        JOIN volunteer v
        ON s.volunteer_id = v.volunteer_id
        WHERE o.org_status_id = 1
        AND v.volunteer_status_id = 1
        GROUP BY s.org_id;
    """
    rows = execute_read_query(conn, query)
    return jsonify(rows)

@app.route('/getEventsHours', methods=['GET'])
def getEventsHours():
    query = """
        SELECT s.event_id, e.event_name, SUM(s.total_hours) AS total_hours_per_event
        FROM session s
        JOIN event e
        ON s.event_id = e.event_id
        WHERE e.event_status_id = 1
        GROUP BY s.event_id;
    """
    rows = execute_read_query(conn, query)
    return jsonify(rows)

@app.route('/getEventsVolunteers', methods=['GET'])
def getEventsVolunteers():
    query = """
        SELECT s.event_id, e.event_name, COUNT(s.volunteer_id) as num_volunteers
        FROM session s
        JOIN event e
        ON s.event_id = e.event_id
        JOIN volunteer v
        ON s.volunteer_id = v.volunteer_id
        WHERE e.event_status_id = 1
        AND v.volunteer_status_id = 1
        GROUP BY s.event_id;
    """
    rows = execute_read_query(conn, query)
    return jsonify(rows)

@app.route('/getEventsHoursVolunteers', methods=['GET'])
def getEventsHoursVolunteers():
    query = """
        SELECT s.event_id, e.event_name, SUM(s.total_hours) AS total_hours_per_event, COUNT(s.volunteer_id) as num_volunteers
        FROM session s
        JOIN event e
        ON s.event_id = e.event_id
        JOIN volunteer v
        ON s.volunteer_id = v.volunteer_id
        WHERE e.event_status_id = 1
        AND v.volunteer_status_id = 1
        GROUP BY s.event_id;
    """
    rows = execute_read_query(conn, query)
    return jsonify(rows)

@app.route('/getDatesHours', methods=['GET'])
def getDatesHours():
    query = """
        SELECT session_date, sum(total_hours) AS total_hours
        FROM session
        GROUP BY session_date
        ORDER BY session_date desc;
    """
    rows = execute_read_query(conn, query)
    return jsonify(rows)

# Volunteer History Page
#total session history from the last six months
@app.route('/get_6months_session_history/<volunteer_id>', methods=['GET'])
def get_volunteer_session_history(volunteer_id):
    print('volunteer_id:', volunteer_id)
    query = """
        select event.event_name as eventName, organization.org_name as orgName, session.total_hours as hours, session.session_date as dateval from session
join event 
on event.event_id = session.event_id
join organization
on organization.org_id = session.org_id
WHERE session_date >= DATE_SUB(NOW(), INTERVAL 6 MONTH)  AND session_date <= NOW() and volunteer_id = '%s';
    """ % volunteer_id
    rows = execute_read_query(conn, query)
    print(rows)
    return jsonify(rows)

#hours per month in the last six months
@app.route('/get_6months_hours_history/<volunteer_id>', methods=['GET'])
def get_volunteer_hours_history(volunteer_id):
    print('volunteer_id:', volunteer_id)
    query = """
        select SUM(session.total_hours) as hours, MONTH(session.session_date) as monthnum, DATE_FORMAT(session.session_date, '%%M') as month, YEAR(session.session_date) as year from session
WHERE session_date >= DATE_SUB(NOW(), INTERVAL 6 MONTH)  AND session_date <= NOW() and volunteer_id = '%s'
GROUP BY month, MONTH(session.session_date), YEAR(session.session_date)
ORDER BY YEAR(session.session_date) DESC, MONTH(session.session_date) DESC;
    """ % volunteer_id
    rows = execute_read_query(conn, query)
    print(rows)
    return jsonify(rows)


if __name__ == "__main__":
    app.run()