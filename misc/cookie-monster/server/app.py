from flask import Flask, request, redirect, render_template, send_from_directory, make_response

app = Flask(__name__,static_folder='static')

@app.route('/')
def index():
    resp = make_response(render_template("index.html"))
    resp.set_cookie("admin","0")
    return resp

@app.route("/robots.txt")
def show_robots():
    return send_from_directory(app.static_folder,"robots.txt")

@app.route("/cookiemonster")
def read_cookie():
   cookie = request.cookies.get("admin")
   if cookie != "1":
       return render_template("cookie.html"), 403
   else:
       return render_template("cookie-flag.html") 


if __name__ == "__main__":
    app.run(host="0.0.0.0")

