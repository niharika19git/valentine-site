from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def card():
    return render_template("card.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/end")
def end():
    return render_template("end.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
