from flask import Flask,render_template

app = Flask(__name__) 

@app.route("/") # route
def home(): #view function
    c = {
        "name" : "aquamen",
        "company" : "dc comis",
        "image" : "https://i.pinimg.com/originals/63/66/cc/6366ccc93c40d19c4ab39a82e78ddcbc.jpg",
        "abilities" : ["speed","strength","reflexes","underwater","telepathy"]
    }
    # character_name = "AQUAMAN"
    # company ="dc comissssssss"
    # image ="https://i.pinimg.com/originals/63/66/cc/6366ccc93c40d19c4ab39a82e78ddcbc.jpg"
    # abilities = ["speed","strength","reflexes","underwater","telepathy"]
    return render_template("home.html",
                            character=c)
                           

@app.route("/c4e")
def c4e():
    return "code for everyone 24"

@app.route("/hi/<name>")
def say_hi(name):
    print(name)
    return "hi " + name

@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    s = a + b
    return str(s)

if __name__ == "__main__":
    app.run(debug=True)