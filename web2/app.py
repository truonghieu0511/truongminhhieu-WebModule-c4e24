from flask import Flask,render_template
app = Flask(__name__)

@app.route("/character")
def character():
    c = {
        "name":"Thannos",
        "image":"https://vignette.wikia.nocookie.net/marvelcinematicuniverse/images/5/52/Empire_March_Cover_IW_6_Textless.png/revision/latest?cb=20180325144529",
        "link":"http://marvelcinematicuniverse.wikia.com/wiki/Thanos",
    }
    c_list = [
        {
            "name":"Thannos",
            "image":"https://vignette.wikia.nocookie.net/marvelcinematicuniverse/images/5/52/Empire_March_Cover_IW_6_Textless.png/revision/latest?cb=20180325144529",
            "link":"http://marvelcinematicuniverse.wikia.com/wiki/Thanos",
        },
        {
            "name":"captain",
            "image":"https://khangvinhrc.net/wp-content/uploads/2018/03/captainamericamohinh4.jpg",
            "link":"https://www.marvel.com/characters/captain-america-steve-rogers",
        },
        {
            "name":"aquamen",
            "image":"https://assets1.ignimgs.com/2018/07/19/q-1532010470464_1280w.jpg",
            "link":"https://www.aquamanmovie.com/",
        },
        {
            "name":"spider man",
            "image":"https://znews-photo.zadn.vn/w480/Uploaded/wyhktpu/2018_12_17/3227afe659fbbaa5e3ea.jpg",
            "link":"https://www.playstation.com/en-us/games/marvels-spider-man-ps4/ ",  
        }
    ]
   
    return render_template("character_list.html",
                            character=c,
                            characters_list=c_list,
                            )

# @app.route("/names")
# def name():
#     c4e_list = ["hieu","huy","huong","duc"]
#     return render_template("names.html",)

food_list = [
        {
            "mon":"bun bo",
            "image":"https://vcdn-ngoisao.vnecdn.net/2018/01/19/1-8515-1516314392.jpg",
            "link":"https://cookpad.com/vn/tim-kiem/b%C3%BAn%20b%C3%B2",
            "yt":"093uwNq5xjg",
        },
        {
            "mon":"bun cha",
            "image":"http://via.placeholder.com/200x200",
            "link":"https://www.google.com/",
            "yt":"pHUPyR6Z0Ds"
            
        },

    ] 
@app.route("/food-items")
def food():
    return render_template("food.html",food_items=food_list)

@app.route("/food_detail/<int:index>")
def food_detail(index):
    f_item = food_list[index]

    return render_template("food_detail.html",food_list=f_item)
  

if __name__ == '__main__':
  app.run(debug=True)