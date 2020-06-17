from flask import Flask, request, make_response,jsonify
from functools import wraps
from otodom import make_url, otodom_scrap

app = Flask(__name__)

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'root' and auth.password == 'root':
            return f(*args, **kwargs)

            return make_response('Could not verify your login!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    return decorated

@app.route('/')
def index():
    if request.authorization and request.authorization.username == 'root' and request.authorization.password == 'root':
        return '<h1> You are logged in</h1>'

    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Requried"'})


@app.route('/api/<cityy>')
@auth_required
def page(cityy):
    temp = make_url(cityy)
    return jsonify(otodom_scrap(temp))

@app.route("/api/<cityy>/<recordNumber>")
@auth_required
def flat_scrap_func(cityy,recordNumber):
    temp = make_url(cityy)
    option=1
    return jsonify(otodom_scrap(temp,recordNumber,option))

if __name__ == "__main__":
    app.run(

    )

