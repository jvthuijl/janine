'''This example demonstrates embedding a standalone Bokeh document
into a simple Flask application, with a basic HTML web form.

To view the example, run:

    python simple.py

in this directory, and navigate to:

    http://localhost:5000

'''
from __future__ import print_function

import flask
import MySQLdb
from flask import request
import json
from datetime import datetime


app = flask.Flask(__name__)

@app.route("/get", methods=['GET'])
def get():
    db = MySQLdb.connect(host="10.202.0.5",
                         user="cover28",
                         passwd="2WLVhdAQZev8ph6v",
                         db="belsimpel")
    cur = db.cursor()
    cur.execute("SELECT searchQuery FROM searchQueries WHERE searchQuery LIKE '%janine%'")
    data = cur.fetchall()

    db.close()

    # for i in range(0, data[0].length):
    #     data[i][1] = int(data[i][1])
    #
    # timestamps_js = []


    # for i in timestamps:
    #     timestamps_js.append(int(i))
    #
    # data_json = {}
    # data_json['lights'] = lights
    # data_json['timestamps'] = timestamps

    return json.dumps(data)

@app.route("/")
def index():
    """ home """
    db = MySQLdb.connect(host="10.202.0.5",
                         user="cover28",
                         passwd="2WLVhdAQZev8ph6v",
                         db="belsimpel")
    cur = db.cursor()
    data = cur.fetchall()

    db.close()

    html = flask.render_template('chart.html', data=json.dumps(data))
    return html

if __name__ == "__main__":
    print(__doc__)
    app.run()