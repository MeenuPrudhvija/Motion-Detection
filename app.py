from flask import Flask, render_template, jsonify
from motion_detection import motionDetection
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start-motion-detection')
def start_motion_detection():
    t = Thread(target=motionDetection)
    t.start()
    return jsonify(message='Motion detection started')

if __name__ == "__main__":
    app.run(debug=True)
