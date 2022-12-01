from flask import Flask, render_template


app=Flask(__name__)

@app.route("/")
def helloworld():
    return "<h1>Hello World</h1>"

@app.route("/color")
def color():
    conn = sqlite.connect("colors.db")
    c = conn.cursor()
    c.execute("SELECT * FROM colors WHERE id = 1;")
    py_color = c.fetchome()

    c.close()

    print(py_color)

    return render_template("colors.html")

@app.route("/template")
def template():
    py_name = "sunabaco"
    return render_template("index.html", name=py_name)

@app.route("/<name>")
def greet(name):
    return name + "さん、こんにちは！"

if __name__=="__main__":
 
    app.run(debug=True)