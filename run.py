import os 

from flask import Flask, render_template


app = Flask(__name__) #so python knows where to find template


@app.route("/")#root directory


def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__": #default module
    app.run(
        host=os.environ.get("IP", "0.0.0.0"), #look for ip but the default is 0.0.0.0
        port=int(os.environ.get("PORT", "5000")), #default to prot 5000
        debug=True)
    