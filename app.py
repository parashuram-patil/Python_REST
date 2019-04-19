import json

from flask import render_template, Flask, request, current_app

app = Flask(__name__, template_folder="templates")


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/print_name/<name>', methods=['GET'])
def print_name(name):
    return 'Hello ' + name + '!!!'


@app.route('/save_name', methods=['PUT'])
def save_name():
    body = request.get_json(silent=True)
    response = 'Hello ' + body["name"] + '!!!'
    return response


@app.route('/validate_name/<name>', methods=['POST'])
def validate_name(name):
    body = request.get_json(silent=True)

    status_code = 200
    response_message = None
    message = None

    if not name == body["param"]:
        status_code = 405
        message = 'param not matching'
    elif not request.headers.get('name') == body["header"]:
        status_code = 406
        message = 'header not matching'
    else:
        message = body

    response_message = {
        "response": message
    }

    response = current_app.response_class(
        json.dumps(response_message),
        status_code,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(debug=True)
