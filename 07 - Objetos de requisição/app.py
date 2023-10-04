from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    t1 = request.args.to_dict()
    t2 = dict(request.args)
    return json.dumps([t2['nome'], t1['idade']])

if __name__ == '__main__':
    app.run()