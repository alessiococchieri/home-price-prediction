from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/hello')
def hello():
    return "hi"

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods = ['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })

    return response

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(port = 8005)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
