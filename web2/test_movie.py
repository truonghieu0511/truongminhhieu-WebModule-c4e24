#1.connect to dâtbase
import mlab
from mongoengine import Document,StringField,IntField

mlab.connect()

#2. define model
class Movie(Document):
    title = StringField()
    image = StringField()
    link = StringField()
    rate = IntField()
movie_list = Movie.objects(rate__gte=7,title__icontains="iron man")#lazy loading
for m in movie_list:
    print(m.title,m.rate)
#3. create data
# m = Movie(title="iron man",
#           image="https://www.sideshowtoy.com/assets/products/903421-iron-man/lg/marvel-avengers-infinity-war-iron-man-sixth-scale-figure-hot-toys-903421-13.jpg",
#           link="https://www.google.com/search?q=aquaman&rlz=1C1CHBF_enVN803VN803&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiU6bWI9tbfAhWZHHAKHdodAD8Q_AUIDygC&biw=1366&bih=657#imgrc=Khd9ggoSO3Jn9M:",
#           rate=7)

# m.save()
