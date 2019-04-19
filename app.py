from flask import render_template, Flask, request

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
    return 'Hello ' + body["name"] + '!!!'


if __name__ == '__main__':
    app.run(debug=True)
