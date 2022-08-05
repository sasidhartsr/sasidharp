import json
from datetime import datetime
import psycopg2
from flask import Flask
from flask_restful import Api
from sqlalchemy import Column, String, Integer, Date, BOOLEAN, and_, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
app = Flask(__name__)
api = Api(app)
Base = declarative_base()
database_url = "postgresql://postgres:1234@localhost:5432/postgres"
engine = create_engine(database_url, echo=True, poolclass=NullPool)
Session = sessionmaker(bind=engine)
session = Session()
class hero1(Base):
    __tablename__ = 'enquiry_test_ride'
    customeNrame = Column("customer_name", String)
    mobileNo = Column("mobile_no", Integer, primary_key=True)
    vehicleModelm = Column("vehicle_modelm", Integer)
    states = Column("states", String)
    district = Column("district", String)
    city = Column("city", String)
    existingVehicle = Column("existing_vehicle", Integer)
    dealerState = Column("dealer_state", String)
    dealerTown = Column("dealer_town", String)
    dealer = Column("dealer",String)
    briefAboutEnquiry = Column("brief_about_enquiry", String)
    expectedDateOfPurchase = Column("expected_date_of_purchase",Integer)
    gender = Column("gender",String)
    age = Column("age", Integer)
    occupation = Column("occupation", String)
    intendedUsage = Column("intended_usage",String)
@app.route('/hero1', methods=['GET'])
def home():
    results = session.query(hero1).all()
    for item in results:
        results_3=[item.__dict__ for item in results]
    for item in results_3:
        del item['_sa_instance_state']
    return json.dumps(results_3)
app.run(debug=True)