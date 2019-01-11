#update,delete
#Atomic
import mlab
from models.character import Character
mlab.connect()
character = Character.objects().with_id("5c34a7658d1556092c59c0d2")
# character.update(set__rate=10,set__name="super super man")
# character.reload()
# print(character.rate)
#1. Update

#1.1 Read document
#1.2 Update document

character.delete()
# 2. Delete
# 2.1 Read document
#2.2 Delete document