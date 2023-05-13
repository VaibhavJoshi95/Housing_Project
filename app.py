from flask import Flask
from housing.logger import logging

app = Flask(__name__)

@app.route("/", methods=['GET','PUSH'])

def index():
    logging.info("We are testing logging project")
    return"Starting Machine LEarning Project"

if __name__== "__main__":
    app.run(debug=True)