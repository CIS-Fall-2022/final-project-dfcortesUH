# David Cortes CIS 3368
# importing functions and classes from the creds and sql files to use with this
import flask
import mysql.connector
import creds
from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execute_read_query
from flask import jsonify
from flask import request

# Setting up the username and password in the beggining to use with the log in functionality
authorizedusers = [
    {
        # default user
        'username': 'davidfcortes007atUH',
        'password': 'finalProjectatUHpu',
        'role': 'default',
        'token': '0',
        'admininfo': None
    }
]

#setting up an application name (REFERENCE: from 5th lecture's py file)
app = flask.Flask(__name__) #sets up the application
app.config["DEBUG"] = True #allow to show errors in browser

#(Reference: security.api file from lecture)
# route to authenticate with username and password
# test in postman by creating header parameters 'username' and 'password' and pass in credentials
@app.route('/', methods=['GET'])
def home():
    username = request.headers['username'] #get the header parameters
    pw = request.headers['password']
    for au in authorizedusers: #loop over all users and find one that is authorized to access
        if au['username'] == username and au['password'] == pw: #found an authorized user
            adminInfo = au['admininfo']
            returnInfo = []
            returnInfo.append(au['role'])
            returnInfo.append(adminInfo)
            return jsonify(returnInfo)
    return 'SECURITY ERROR'

# -FUNCTIONS FOR AIRPORTS-

# add airport record to airport table (REFERENCE: from 5th lecture's py file)
@app.route('/api/airports/post', methods=['POST'])
def add_airport_record():
    request_data = request.get_json() # Request data for each part of the airport we want to add to the airports table.
    airportcode = request_data['airportcode']
    airportname = request_data['airportname']
    country = request_data['country']
    myCreds = creds.Creds()
    airports = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    add_airport_query = "INSERT INTO airports (airportcode,airportname,country) VALUES (%s, '%s', '%s')" % (airportcode,airportname,country)
    execute_query(airports, add_airport_query)   
    return 'Airport added!'

# read record from airports(REFERENCE: from 5th lecture's py file)
@app.route('/api/airports/get', methods=['GET'])
def read_airports_records():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "SELECT * FROM airports"
    airports = execute_read_query(conn, sql)
    return jsonify(airports)

# update an airport's country (REFERENCE: from 5th lecture's py file)
@app.route('/api/airports/put', methods=['PUT'])
def update_airports_record():
    request_data = request.get_json()   
    id_for_airport = request_data['id']  # Requesting data from Postman to get info on which record to update and value to update it with.
    new_country = request_data['country']
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    update_airport_query = """
    UPDATE airports
    SET country = '%s'
    WHERE id = %s """ % (new_country, id_for_airport)
    execute_query(conn, update_airport_query)
    return 'Airport country updated!'

# delete airport from airport table (REFERENCE: from 5th lecture's py file)
@app.route('/api/airports/delete', methods=['DELETE'])
def delete_airports_record():
    request_data = request.get_json()
    airport_id_to_delete = request_data['id']   # Requesting data from Postman to get info on which record to delete.
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    delete_airport_query = "DELETE FROM airports WHERE id = %s" % (airport_id_to_delete)
    execute_query(conn, delete_airport_query)
    return 'Airport deleted!'

# -FUNCTIONS FOR PLANES-
# add plane record to planes table (REFERENCE: from 5th lecture's py file)
@app.route('/api/planes/post', methods=['POST'])
def add_planes_record():
    request_data = request.get_json() # Request data for each part of the plane we want to add to the plane table.
    make = request_data['make']
    model = request_data['model']
    year = request_data['year']
    capacity = request_data['capacity']
    myCreds = creds.Creds()
    planes = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    add_planes_query = "INSERT INTO planes (make,model,year,capacity) VALUES ('%s', '%s', %s, %s)" % (make,model,year,capacity)
    execute_query(planes, add_planes_query)   
    return 'Plane added!'

# read record from planes(REFERENCE: from 5th lecture's py file)
@app.route('/api/planes/get', methods=['GET'])
def read_planes_records():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "SELECT * FROM planes"
    planes = execute_read_query(conn, sql)
    return jsonify(planes)

# update planes country (REFERENCE: from 5th lecture's py file)
@app.route('/api/planes/put', methods=['PUT'])
def update_planes_record():
    request_data = request.get_json()   
    plane_id = request_data['id']  # Requesting data from Postman to get info on which record to update and value to update it with.
    new_plane_year = request_data['year']
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    update_planes_query = """
    UPDATE planes
    SET year = %s
    WHERE id = %s """ % (new_plane_year, plane_id)
    execute_query(conn, update_planes_query)
    return 'Planes year updated!'

# delete plane record from the planes table (REFERENCE: from 5th lecture's py file)
@app.route('/api/planes/delete', methods=['DELETE'])
def delete_plane_record():
    request_data = request.get_json()
    plane_id_to_delete = request_data['id']   # Requesting data from Postman to get info on which record to delete.
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    delete_airport_query = "DELETE FROM planes WHERE id = %s" % (plane_id_to_delete)
    execute_query(conn, delete_airport_query)
    return 'Plane deleted!'

# -FUNCTION FOR FLIGHTS-
# add flight record to flights table (REFERENCE: from 5th lecture's py file)
@app.route('/api/flights/post', methods=['POST'])
def add_flight_record():
    request_data = request.get_json() # Request data for each part of the flight we want to add to the flight table.
    planeid = request_data['planeid']
    airportfromid = request_data['airportfromid']
    airporttoid = request_data['airporttoid']
    date = request_data['date']
    myCreds = creds.Creds()
    flights = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    add_flight_query = "INSERT INTO flights (planeid,airportfromid,airporttoid,date) VALUES (%s, %s, %s, %s)" % (planeid,airportfromid,airporttoid,date)
    execute_query(flights, add_flight_query)   
    return 'Flight added!'

# read record from planes(REFERENCE: from 5th lecture's py file)
@app.route('/api/flights/get', methods=['GET'])
def read_flights_records():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "SELECT * FROM flights"
    flights = execute_read_query(conn, sql)
    return jsonify(flights)

# delete plane record from the planes table (REFERENCE: from 5th lecture's py file)
@app.route('/api/flights/delete', methods=['DELETE'])
def delete_flight_record():
    request_data = request.get_json()
    flight_id_to_delete = request_data['id']   # Requesting data from Postman to get info on which record to delete.
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    delete_flight_query = "DELETE FROM flights WHERE id = %s" % (flight_id_to_delete)
    execute_query(conn, delete_flight_query)
    return 'Flight deleted!'

app.run()