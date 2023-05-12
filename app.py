from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET','PUSH'])

def index():
    return"Starting Machine LEarning Project"

if __name__== "__main__":
    app.run(debug=True)