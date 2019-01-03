from flask import Flask , render_template

app = Flask(__name__)
@app.route('/user/<username>')
def user(username):
    users = {
        "hieu" : {
            "name" : "Hiếu",
            "gender" : "male",
            "age" : 21,
            "hobbies" : "chơi game , du lịch , đá bóng"
        },
        "nga" : {
            "username" : "nga",
            "name" : "Nga",
            "gender" : "lgbt",
            "age" : 20,
            "hobbies" : "xem phim , nghe nhạc"
        } 
    }
    return render_template("user.html",users=users,username=username)
if __name__ == '__main__':
    app.run(debug=True)