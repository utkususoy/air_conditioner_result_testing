from flask import Flask, jsonify, request, render_template
import energy_consumption_loader
import repository
from flask_pymongo import pymongo

app = Flask(__name__)
res = ""
isReload = "0"

selected_attributes = {
    "temp": "",
    "valv": "",
    "fan": "",
    "isUpdate": isReload
}

tempretures = [
    {"val": "---Sıcaklık seç---"},
    {"val": "20"},
    {"val": "21"},
    {"val": "22"},
    {"val": "23"},
    {"val": "24"},
    {"val": "25"},
]

valves = [
    {"val": "---Vana seç---"}
]

fans = [
    {"val": "---Fan seç---"}
]

def generate_params(feature_dict, param_range):
    for i in range(param_range[0], param_range[1]):
        feature_dict.append({'val': str(i)})
    return feature_dict

valves = generate_params(valves, [30, 81])

fans = generate_params(fans, [60, 101])



@app.route("/")
def welcome_page():
    global res
    print("welcome_page")
    return render_template("index.html")

@app.route("/load")
def load_values():
    return jsonify({'temps': tempretures, 'valves': valves, 'fans': fans})

@app.route("/", methods=['POST'])
def make_predict():
    global selected_attributes

    request_data_temp = request.form['option_1']
    request_data_valv = request.form['option_2']
    request_data_fan = request.form['option_3']

    selected_attributes['temp'] = request_data_temp
    selected_attributes['valv'] = request_data_valv
    selected_attributes['fan'] = request_data_fan

    try:
        global res
        prediction_value = energy_consumption_loader.predictor([int(request_data_temp),
                                         int(request_data_valv),
                                         int(request_data_fan)])

        return render_template("evaluate.html", tempretures= {"temp": request_data_temp, "valv": request_data_valv,
                                                       "fan": request_data_fan, "res":"{:.2f}".format(prediction_value)} )
    except Exception as e:
        return "{}".format(e)

@app.route("/save", methods=['POST'])
def save_values():
    repo = repository.Mongo_db_repository()
    request_data = request.get_json()
    repo.insert_records(request_data)
    return "ok"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port = 3000)