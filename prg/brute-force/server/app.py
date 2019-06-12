from flask import Flask, request, redirect, render_template, send_from_directory, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/4936")
def flag():
    return 'STRT{pure_brute_force_works}'

if __name__ == "__main__":
    app.run()

