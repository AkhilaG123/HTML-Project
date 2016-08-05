from flask import render_template
from WEBpages import app
@app.route('/')
def main():
    return render_template("layout.html")

