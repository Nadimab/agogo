
from flask import Flask, request, jsonify
# from flask_cors import CORS

# from flask_sqlalchemy import SQLAlchemy
# import psycopg2

# app = Flask(__name__)
# CORS(app)
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/Agogo'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # db = SQLAlchemy(app)

# # class patient_static_info(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     first_name = db.Column(db.String(80), unique=True, nullable=False)
# #     last_name = db.Column(db.String(80), unique=True, nullable=False)
# #     gender = db.Column(db.String(80), unique=True, nullable=False)
# #     date_of_birth = db.Column(db.Date, unique=True, nullable=False)
# #     phone = db.Column(db.String(80), unique=True, nullable=False)
# #     email = db.Column(db.String(80), unique=True, nullable=False)
# #     address = db.Column(db.String(80), unique=True, nullable=False)

# #     def __init__(self, id, first_name, last_name,  gender, date_of_birth, phone, email, address):
# #         self.id = id
# #         self.first_name = first_name
# #         self.last_name = last_name
# #         self.gender = gender
# #         self.date_of_birth = date_of_birth
# #         self.phone = phone
# #         self.email = email
# #         self.address = address

    
# @app.route('/',methods=['POST'])
# def index():
#     data = request.data
#     print(data.type)
#     return jsonify('Hello World')

# if __name__ == '__main__':
#     app.run(debug=True)

