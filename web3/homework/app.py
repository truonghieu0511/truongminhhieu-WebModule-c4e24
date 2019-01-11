from flask import *
from models.river import River
import mlab
app = Flask(__name__)
mlab.connect()

@app.route('/river/Africa')
def river_africa():
    river_list = River.objects(continent='Africa')
    return render_template("river.html",river_list=river_list)
def river_samerica():
    river_list = River.objects(continent='S.America',length__lt=100)
    return render_template('river.html',river_list=river_list)
if __name__ == '__main__':
    app.run(debug=True)