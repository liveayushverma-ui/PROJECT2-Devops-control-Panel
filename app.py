from flask import Flask, render_template, jsonify
import psutil
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/metrics")
def metrics():
    data = {
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
        "hostname": socket.gethostname(),
        "time": str(datetime.datetime.now())
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
