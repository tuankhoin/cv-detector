from flask import Flask, render_template, Response, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect')
def detect():
    return render_template('detect.html')

@app.route('/heatmap')
def heatmap():
    return render_template('heatmap.html')

@app.route('/mask')
def mask():
    return render_template('mask.html')

if __name__=='__main__':
    app.run(debug=True)
