import json
import os
import psycopg2
from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import JSON

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(
        host="localhost",
        database="Agogo",
        # user=os.environ['DB_USERNAME'],
        # password=os.environ['DB_PASSWORD']
        user="postgres",
        password="postgres"
        )

# @app.route('/patient', methods=['POST'])
# def patient():
#     data = request.data
#     # cur = conn.cursor()
#     # cur.execute('')
#     # books = cur.fetchall()
#     # cur.close()
#     # conn.close()
#     return jsonify(data)





# @app.route('/', methods=['POST'])
# def index():
#     # data = request.data
#     # conn = get_db_connection()
#     # cur = conn.cursor()
#     # cur.execute('SELECT * FROM dietitian;')
#     # books = cur.fetchall()
#     # cur.close()
#     # conn.close()
#     print(request)
#     return jsonify('Hello World!')

@app.get('/patient')
def patient():
    cur = conn.cursor()
    cur.execute( 'select patient_id ,first_name as patientFullName,last_name ,gender , cast (date_of_birth as text), phone ,email ,address ,dietitian_id from patient_static_info;')

    r = [dict((cur.description[i][0], value) \
                for i, value in enumerate(row)) for row in cur.fetchall()]
    
    print(r)
    cur.close()
    return r

@app.post('/patient')
def patientPost():
    # request to json
    data = request.get_json()
    print("data: " )
    # print(data.patientFullName)
    print (data['patientFullName'])
    cur = conn.cursor()
    cur.execute('INSERT INTO patient_static_info (first_name,last_name,gender,date_of_birth,phone,email,address,dietitian_id)'
            'VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
            (data['patientFullName'],
             'test',
             data['patientGender'],
             data['patientDateOfBirth'],
             data['patientPhone'],
             data['patientEmail'],
             data['patientAddress'],
             1)
            )
    cur.close()
    conn.commit()
    print ('done')
    return jsonify('post hello')