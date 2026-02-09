from flask import Flask, render_template

# create the website app
app = Flask(__name__)

# first page (card)
@app.route("/")
def card():
    return render_template("card.html")

# second page (gallery)
@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

# third page (final heart)
@app.route("/end")
def end():
    return render_template("end.html")

# run the website
app.run(debug=True, host="0.0.0.0", port=5000)
