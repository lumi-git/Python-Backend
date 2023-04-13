from flask import Flask,request
from flasgger import LazyJSONEncoder
from flask_cors import CORS 

app = Flask("main")
app.json_encoder = LazyJSONEncoder

#Ici on autorise des appels de requêtes de n'importe quelle origine
CORS(app)

@app.route("/")
def root():
    tab = [1, 2, 3]
    return {"hello": "world", "tab": tab}


@app.route("/test")
def test():
    tab = [1, 2, 3]
    return {"test": "test"}


@app.route("/sendInfo", methods=["POST"])
def receiveInfo():
    username = request.json["Username"]
    password = request.json["Password"]
    print(f"Username recieved {username}" )
    print(f"Password recieved {password}" )
    if username == "admin" and password == "admin":
        print("Authorized")
        return {"status": "Authorized"}
    else:
        print("Refused")
        return {"status": "Refused"}
