
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func ,inspect

from flask import Flask, jsonify


engine = create_engine("sqlite:///hawaii-3.sqlite 2")
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()
measurement = Base.classes.measurement
station = Base.classes.station

session = Session(engine)

inspector = inspect(engine)
inspector.get_table_names()


app = Flask(__name__)



#routes
@app.route("/")
def home():
    return("/api/v1.0/precipitation<br/>"
    "/api/v1.0/stations<br/>"
    "/api/v1.0/tobs<br/>"
    "/api/v1.0/2017-01-01<br/>")

@app.route("/api/v1.0/precipitation")
def precipitation():
    que = session.query(measurement.date, measurement.prcp).filter(measurement.date>="2016-08-23").all()
    result = list(np.ravel(que))
    return jsonify(result)



@app.route("/api/v1.0/stations")
def stations():
    que = session.query(station.station, station.name).all()
    result1 = list(np.ravel(que))
    return jsonify(result1)




@app.route("/api/v1.0/tobs")
def tobs():
    que = session.query(measurement.date, measurement.tobs).filter(measurement.date>="2016-08-23").filter(measurement.date<="2017-08-23").all()
    result2 = list(np.ravel(que))
    return jsonify(result2)


@app.route("/api/v1.0/<date>")

def start1(date):

    que = session.query((measurement.date, func.avg(measurement.tobs), func.max(measurement.tobs), func.min(measurement.tobs)).filter(measurement.date)>=date).all()
    result3 = []
    for i in que:

        dict = {}
        dict["Date"] = i.Date
        dict["Avg"] = i.func.avg(Measurement.tobs)
        dict["Min"] = i.func.min(Measurement.tobs)
        dict["Max"] = i.func.max(Measurement.tobs)
        result4.append(dict)

    return jsonify(result4)


    
if __name__ == '__main__':
    app.run(debug=True)