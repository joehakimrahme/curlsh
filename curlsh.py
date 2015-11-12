from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def hello():
    ua = request.headers.get('User-Agent')

    if ua.lower().startswith('curl'):
        return "Evil script\n"
    else:
        return "Hello World!\n"


if __name__ == "__main__":
    app.run()
