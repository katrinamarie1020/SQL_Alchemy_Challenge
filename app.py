import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    """Return a list of all precipitation"""

    # Calculate the date 1 year ago from the last data point in the database
    last_date = '2016-08-23'
    # Perform a query to retrieve the date and precipitation scores
    rain_12 = session.query(Measurement.prcp, Measurement.date).filter(Measurement.date >last_date).all()

    session.close()

    # Convert list of tuples into normal list
    all_prcp = list(np.ravel(rain_12))

    return jsonify(all_prcp)


@app.route("/api/v1.0/stations")
def station():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    results = session.query(Station.station).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    stations = list(np.ravel(results))

    return jsonify(stations)

@app.route("/api/v1.0/tobs")

def tobs():
    session = Session(engine)

    last_date = '2016-08-23'
    
# Perform a query to retrieve the date and precipitation scores
    tobs_12 = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >=last_date).all()

    session.close()

    tobs_results = list(np.ravel(tobs_12))

    return jsonify(tobs_results)


@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")

def temps(start, end):
    session = Session(engine)

    temp_result = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    session.close()

    temp_result2 = list(np.ravel(temp_result))

    return jsonify(temp_result2)


if __name__ == '__main__':
    app.run(debug=True)


