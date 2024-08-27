from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/chat")
def chat():
    username = 

if __name__ == "__main__":
    app.run(debug=True)