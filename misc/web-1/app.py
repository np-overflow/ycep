from flask import Flask, request, redirect, render_template, send_from_directory, make_response

app = Flask(__name__,static_folder='static')

@app.route('/')
def index():
    resp = make_response(render_template("index.html"))
    resp.set_cookie("admin","0")
    return resp

# Challenge one
@app.route("/agents")
def user_agent():
    user_agent = request.headers.get("User-Agent")
    if user_agent == "YCEPBot":
        return render_template("agent-flag.html")
    else:
        return render_template("agent-fail.html",user_agent = user_agent)

# Challenge two
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
    app.run()

