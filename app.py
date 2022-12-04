from flask import Flask, render_template
import sqlite3, random

app=Flask(__name__)

@app.route("/")
def helloworld():
    return "<h1>Hello World</h1>"

@app.route("/color1")
def color1():
    py_color = "青"
    return render_template("color copy.html", color =py_color)

@app.route("/color")
def color():
    conn = sqlite3.connect("color.db")
    c = conn.cursor()
#    c.execute("SELECT * FROM colors WHERE id = 1;")
    c.execute("SELECT * FROM colors;")

#    py_color = c.fetchone()
    py_color = c.fetchall()
    py_color = random.choice(py_color)

    c.close()

    print(py_color)

    return render_template("color.html", color = py_color)


@app.route("/template")
def template():
    py_name = "sunabaco"
    return render_template("index.html", name=py_name)

#@app.route("/<name>")
#def greet(name):
#    return name + "さん、こんにちは！"

# ToDo
# タスクの追加機能
# 入門フォーム表示
@app.route("/add", methods=["GET"])
def add_get():
    return render_template("add.html")

# 
@app.route("/add", methods=["POST"])
def add_post():
    return render_template("add.html")

if __name__=="__main__":
    app.run(debug=True)