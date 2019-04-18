from flask import render_template, Flask

app = Flask(__name__, template_folder="templates")


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/print_name/<name>', methods=['GET'])
def print_name(name):
    return 'Hello ' + name + '!!!'


if __name__ == '__main__':
    app.run(debug=True)
