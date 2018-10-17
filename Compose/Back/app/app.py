import  socket
from flask import Flask
from model import db_select db_create
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def get():
    return "Hello Word"
@app.route("/competidor")
def competidor():
    db_create()
    array = db_select()
    print(array)
    return jsonify(array)
if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)    