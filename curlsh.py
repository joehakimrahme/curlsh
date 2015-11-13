from flask import Flask, request
app = Flask(__name__)


@app.route("/install.sh")
def hello():
    ua = request.headers.get('User-Agent')

    if ua.lower().startswith('curl'):
        return "echo \"This is malicious code executed, you're logged in as user $(whoami) and running $(uname -a)\"\n"
    else:
        return "echo 'This is a harmless script'\n"


@app.route("/")
def nothing():
    return "SUCCESS"

@app.route("/dont-curl-sh")
def dont_curl_sh():
    with open("/var/www/curlsh/dontcurlsh.md") as article:
        text = """<!DOCTYPE html>
<html>
<title>Don't curl http://example/install.sh | sh</title>

<xmp theme="simplex" style="display:none;">"""
        text += "".join(article.read())
        text += """</xmp>

<script src="http://strapdownjs.com/v/0.2/strapdown.js"></script>
</html>"""
        return text

if __name__ == "__main__":
    app.run()
