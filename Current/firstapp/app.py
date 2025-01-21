from flask import Flask, request # import flask in order to use flask

app = Flask(__name__) # creates our flask application

# 200 status code -> everything went fine
# 300 status code -> are for redirection
# 400 status code -> YOU DID SOMETHING WRONG
# 500 status code -> Server messed something up


# simple url ------------------------
@app.route("/")
def index():
    return "<h1>Hello World</h1>"


@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return "You made a GET request\n"
    elif request.method == "POST":
        return "You made a POST request\n"
    

# ---------------------------------------

# DYNAMIC URLs ----------------------------------------------
@app.route("/greet/<name>")   # <name> is a url processor
def greet(name):
    return f"Hello {name}"

@app.route("/add/<int:number1>/<int:number2>") # this is how you stricken the route to solely integers
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}" # it shows here that the integers will be interpreted. Thus, string concatonation will not take place.


@app.route("/handle_url_params")
def handle_params():
    if "greeting" in request.args.keys() and "name" in request.args.keys():
        greeting = request.args.get("greeting")
        name = request.args.get("name")
        return f"{greeting}, {name}"
    else:
        return "Some parameters are missing"

# --------------------------------------------------------------------

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True) # where and how we run the server 