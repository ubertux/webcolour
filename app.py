from flask import Flask, render_template
import os
import datetime
import socket
import json

app_port = 8080

host = socket.gethostname()

app = Flask(__name__)

@app.route('/')
def main():
    date = datetime.datetime.now()
    return 'Hello, World! from ' + str(host) + " ! " + \
            'Time is now: ' + str(date) + '\n'

@app.route("/hru")
def hello():
   return "I am good, how about you?\n"

@app.route("/env")
def env():
    return json.dumps(dict(os.environ))

@app.route("/red")
def red():
    return render_template('red.html', date=datetime.datetime.now(), hostname=host)

@app.route("/blue")
def blue():
    return render_template('blue.html', date=datetime.datetime.now(), hostname=host)

@app.route("/green")
def green():
    return render_template('green.html', date=datetime.datetime.now(), hostname=host)

@app.route("/yellow")
def yello():
    return render_template('yellow.html', date=datetime.datetime.now(), hostname=host)

@app.route("/pink")
def pink():
    return render_template('pink.html', date=datetime.datetime.now(), hostname=host)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=app_port)
