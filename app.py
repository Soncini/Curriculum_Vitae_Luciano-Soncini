from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route("/")
def index():
    return render_template("index.html")

# Route for the ideas overview
@app.route("/ideas")
def ideas():
    return render_template("ideas.html")

# Route for the contato
@app.route("/contato")
def contato():
    return render_template("contato.html")

# Routes for each individual idea
@app.route("/ideas/hurricanes")
def hurricanes():
    return render_template("hurricanes.html")

@app.route("/ideas/fires")
def fires():
    return render_template("fires.html")

@app.route("/ideas/tesla")
def tesla():
    return render_template("tesla.html")

@app.route("/ideas/space")
def space():
    return render_template("space.html")

@app.route("/ideas/solar")
def solar():
    return render_template("solar.html")

if __name__ == "__main__":
   # app.run(debug=True)
    app.run(host='10.0.0.170', port=5000, debug=True)
