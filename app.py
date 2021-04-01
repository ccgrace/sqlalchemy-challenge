from flask import Flask, jsonifyimport numpy as npimport pandas as pdimport datetime as dtimport sqlalchemyfrom sqlalchemy.ext.automap import automap_basefrom sqlalchemy.orm import Sessionfrom sqlalchemy import create_engine, func, inspect################################################## Database Setup################################################## create engine to hawaii.sqliteengine = create_engine("sqlite:///Resources/hawaii.sqlite")# reflect an existing database into a new modelbase = automap_base()# reflect the tablesbase.prepare(engine, reflect=True) # Save references to each tableMeasurement = base.classes.measurementStation = base.classes.station################################################## Flask Setup#################################################app = Flask(__name__)################################################## Flask Routes#################################################@app.route("/")def home():    """List all available api routes."""        return (            f"/api/v1.0/precipitation<br/>"            f"/api/v1.0/stations<br/>"            f"/api/v1.0/tobs<br/>"            f"/api/v1.0/<start><br/>"            f"/api/v1.0/<start>/<end>")@app.route("/api/v1.0/precipitation")def precipitation():    # Create our session (link) from Python to the DB    session = Session(engine)        """Return a list of PRCPs for each date."""    results = session.query(Measurement.date, Measurement.prcp).all()        precipitation = []        for date, prcp in results:        precip_dict = {}        precip_dict['date'] = date        precip_dict['prcp'] = prcp        precipitation.append(precip_dict)            session.close()            return jsonify(precipitation)    @app.route("/api/v1.0/stations")def station():    # Create our session (link) from Python to the DB    session = Session(engine)        """Return a list of stations."""    results = session.query(Station.station, Station.name).all()        stations = []        for station, name in results:        station_dict = {}        station_dict['station'] = station        station_dict['name'] = name        stations.append(station_dict)            session.close()            return jsonify(stations)        # Create our session (link) from Python to the DB    session = Session(engine)        """Return a list of stations."""    results = session.query(Station.station, Station,name).all()        stations = []        for station, name in results:        station_dict = {}        station_dict['station'] = station        station_dict['name']if __name__ == "__main__":    app.run(debug=True)