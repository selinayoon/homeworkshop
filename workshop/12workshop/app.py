from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/workshop12")
def workshop12():
    return render_template("workshop12.html")


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)
