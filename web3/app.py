from flask import Flask , render_template , request
from models.character import Character
import mlab
mlab.connect()
app = Flask(__name__)

#character.objects() lấy tất cả 
@app.route('/add_character',methods=['GET','POST'])
def add_character():
    #1 gửi form (GET)
    if request.method == "GET":
        return render_template("character_form.html")
    elif request.method == "POST":
    #4 nhận form => lưu (POST)
        form = request.form
        name = form["name"]
        image = form["image"]
        rate = form["rate"]
        new_character = Character(name=name,image=image,rate=rate)
        new_character.save()
        print(name,image,rate)
        #create
        #update
        return "Gotcha"
#list (master)
@app.route('/characters') # hiển thị tất cả các nhân vật 
def characters():
    #1.lấy tất cả các dữ liệu liên quan (database) 
    n = Character.objects()
    #2. render:
    return render_template("view_character.html",n=n )

@app.route("character/<id>")
def character_detail(id):
    #1.get one character, based on given id
    character = Character.objects(id=id.first()) #
    #2.Render:template + data
    return "hahaha"

    

if __name__ == '__main__':
  app.run(debug=True)