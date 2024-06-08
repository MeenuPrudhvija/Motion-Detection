from flask import Flask, render_template, jsonify
from motion_detection import motionDetection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('template/index.html')

@app.route('/start-motion-detection')
def start_motion_detection():
    motionDetection()
    return jsonify(message='Motion detection completed')

if __name__ == "__main__":
    app.run(debug=True)
