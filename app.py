from flask import Flask



app=Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello World"

@app.route("/template")
def template():
    py_name = "あき"
    return render_template("index.html",name=py_name)

@app.route("/<name>")
def greet(name):
    return name + "さん、こんにちは！"

if __name__=="__main__":
 
    app.run(debug=True)