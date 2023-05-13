from flask import Flask
from housing.logger import logging
import sys
from housing.exception import HousingException
app = Flask(__name__)

@app.route("/", methods=['GET','PUSH'])

def index():
    try:
        raise Exception("WE are testng custom execption")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("We are testing logging project")
    return "CI CD pipeline established"

if __name__== "__main__":
    app.run(debug=True)