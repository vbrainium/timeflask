from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello this is the main page from v3"

@app.route("/time")

def current_time():
    format = '%Y-%m-%d %H:%M:%S'
    IST = pytz.timezone('Asia/Kolkata')
    UST = pytz.timezone('Europe/Kiev')
    CST = pytz.timezone('America/Chicago')

    output = f"Local Time is <h2>{datetime.now().strftime(format)}</h2><br>" \
             f"Time in Minneapolis is <h2>{datetime.now(CST).strftime(format)}</h2><br>"\
             f"Time in India is <h2>{datetime.now(IST).strftime(format)}</h2><br>"\
             f"Time in Ukraine is <h2>{datetime.now(UST).strftime(format)}</h2><br>"

    return output

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=5050)