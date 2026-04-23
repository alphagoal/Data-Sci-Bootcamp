from flask import Flask

app = Flask(__name__)
# recreate the flask app


@app.route("/")
# whenever someone calls the "/" path
def hello_world():
    return "<p>Hello, World!</p>"


@app. route ("/page2")
def hello_world2():
    return "This is page2."


app.run(port=9999)
