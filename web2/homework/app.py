from flask import Flask , render_template ,  redirect , request
import mlab
from mongoengine import Document , StringField , IntField , EmailField
app = Flask(__name__)
class User(Document):
            name = StringField()
            email = EmailField()
            username = StringField()
            password = StringField()
        
@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login" ,methods=["GET","POST"])
def login():
    if request.method == "POST":
        user = User(
            name = request.form["name"],
            email = request.form["email"],
            username = request.form["username"],
            password = request.form["password"]
        )
        mlab.connect()
        user.save()
    return render_template("login.html")
if __name__ == '__main__':
    app.run(debug=True)


