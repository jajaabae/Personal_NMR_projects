# File: hello_world.py
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)
import uuid

import os
#from temperature_CO2_plotter import plot_CO2, plot_temperature
from flask import send_from_directory
import shutil

from InformationObject import InformationObject

@app.route("/")
def root():
    return render_template('index.htm')

# No caching:
@app.after_request
def apply_caching(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    return response


from webPage_requests_CreationOfROESYSpectra import webPage_requests_CreationOfROESYSpectra
@app.route("/grid_plotter/", methods=['GET','POST'])
@app.route("/grid_plotter", methods=['GET','POST'])
def another():
    #spec_type = request.args.get("spec_type")
    #print 'spec_type:', spec_type
    #a_tmp = 'HELLO THERE'+spec_type
    information_instance = InformationObject()
    if request.method == 'POST':
        information_instance.datalists = request.form['datalists']
        information_instance.x_list = request.form['x_list']
        information_instance.y_list = request.form['y_list']
        information_instance.x_diameter = request.form['x_diameter']
        information_instance.y_diameter = request.form['y_diameter']
        information_instance.spec_type = request.args.get("spec_type")
        information_instance.intensity_multiplication_variable = request.form['intensity_multiplication_variable']
        
        figureName, figureName2 = webPage_requests_CreationOfROESYSpectra(
            datalists=request.form['datalists'],
            x_list=request.form['x_list'],
            y_list=request.form['y_list'],
            x_diameter=request.form['x_diameter'],
            y_diameter=request.form['y_diameter'],
            spec_type=request.args.get("spec_type"),
            intensity_multiplication_variable=request.form['intensity_multiplication_variable'],
            information_instance = information_instance
            )
        
        return render_template('grid_plotter.htm',
                               datalists=request.form['datalists'],
                               x_list=request.form['x_list'],
                               y_list=request.form['y_list'],
                               x_diameter=request.form['x_diameter'],
                               y_diameter=request.form['y_diameter'],
                               pictureName=figureName,
                               pictureName2=figureName2,
                               spec_type=request.args.get("spec_type"),
                               intensity_multiplication_variable=request.form['intensity_multiplication_variable'],
                               #tmp_val=a_tmp,
                               hasdata='y',
                               )
    else:
        #information_instance.datalists = request.form['datalists']
        information_instance.x_list = "4.13 8.83"
        information_instance.spec_type = request.args.get("spec_type")
        information_instance.intensity_multiplication_variable = 10
        return render_template('grid_plotter.htm',
                               intensity_multiplication_variable=10,
                               x_list = "4.13 8.83",
                               spec_type=request.args.get("spec_type"),
                               information_instance = information_instance)


@app.route("/docs/", methods=['GET'])
@app.route("/docs", methods=['GET'])
def docs():
    return render_template('temperature_CO2_plotter.html')

if __name__ == "__main__":
    debug=False
    debug=True
    #if debug:
    #    import make_doc
    app.run(debug=debug, port=5002)

    #app.run(debug=False, port=5003)
    #app.run(debug=True, host='0.0.0.0') ## DANGER! Available for others on the network











