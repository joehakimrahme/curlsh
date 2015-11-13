from flask import Flask, request
app = Flask(__name__)


@app.route("/install.sh")
def hello():
    ua = request.headers.get('User-Agent')

    if ua.lower().startswith('curl'):
        return "Evil script\n"
    else:
        return "Hello World!\n"


@app.route("/")
def nothing():
    return "SUCCESS"

@app.route("/dont-curl-sh")
def dont_curl_sh():
    with open("dontcurlsh.md") as article:
        text = """<!DOCTYPE html>
<html>
<title>Hello Strapdown</title>

<xmp theme="united" style="display:none;">"""
        text += article.read()
        text += """</xmp>

<script src="http://strapdownjs.com/v/0.2/strapdown.js"></script>
</html>"""
        return text

if __name__ == "__main__":
    app.run()
