import  socket
from flask import Flask
from model import db_select
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def get():
    return "Hello Word"
@app.route("/competidor")
def competidor():
    array = db_select()
    print(array)
    return jsonify(array)
if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)    