import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World from Flask! Wow, that\'s the Internet!'

@app.route('/different')
def different():
    return 'Hello from a dIfFeRenT page!'

@app.route('/gus-wanderings')
def whatever():
    # check database for walks
    # format walks into readable form
    return 'Daily walks around the lake: [list of walks]'

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
