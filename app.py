from flask import Flask, render_template, jsonify
import json
app = Flask(__name__)

@app.route('/issues')
def issues():
    return render_template('issues.html')
@app.route('/get_issues')
def get_issues():
    try:
        with open('json/issues.json') as file:
            issues = json.load(file)
            print (issues)
            return jsonify(issues)
    # if you dont do this and the file doesn't exist, everything crashes
    except FileNotFoundError:
        return "Issues file not found", 404

@app.route('/get_room_config')
def get_room_config():
    try:
        with open('json/config.json') as file:
            room_config = json.load(file)
            print (room_config)
            return jsonify(room_config)
    except FileNotFoundError:
        return "Room config file not found", 404

@app.route('/inventory')
#def is a function
def inventory():
    return render_template('inventory.html')
@app.route('/get_inventory')
#def is a function
def get_inventory():
    try:
        # open the JSON as a temporary fake file. Store the data in a variable
        # with is how it works (nog opzoeken)
        with open('json/inventory.json') as file:
            # store all loaded data in inventory variable and print
            inventory = json.load(file)
            print (inventory)
            # jsonify the data
            return jsonify(inventory)
    except FileNotFoundError:
        return "Inventory file not found", 404

# standard route, calls HTML page
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # run on all IP, run on port 5000
    app.run(host="0.0.0.0", debug=True)
