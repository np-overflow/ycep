from flask import Flask, request, redirect, render_template, send_from_directory, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/agents")
def user_agent():
    user_agent = request.headers.get("User-Agent")
    if user_agent == "YCEPBot":
        return render_template("agent-flag.html")
    else:
        return render_template("agent-fail.html",user_agent = user_agent)

if __name__ == "__main__":
    app.run()

