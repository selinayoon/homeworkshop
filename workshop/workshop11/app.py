from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/workshop11")
def workshop11():
    return render_template("workshop11.html")


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)
