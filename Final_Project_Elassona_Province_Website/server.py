from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/services")
def services():
    return render_template('services.html')

@app.route("/guide")
def guide():
    return render_template('guide.html')

@app.route("/gallery")
def gallery():
    return render_template('gallery.html')

@app.route("/history")
def history():
    return render_template('history.html')

@app.route("/transportation")
def transportation():
    return render_template('transportation.html')

@app.route("/contact_us")
def contact_us():
    return render_template('contact_us.html')