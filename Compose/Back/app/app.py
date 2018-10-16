import  socket
from flask import Flask
#from flask.ext.jsonpify import jsonify

app = Flask(__name__)

@app.route("/")
def get():
    return "Hello Word"

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)    