
from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.template_folder="html"
Bootstrap(app)

@app.route("/index")
def index():
    return render_template("base_boot.html")


app.run(debug=True)

