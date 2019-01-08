import mongoengine
#mongodb://<dbuser>:<dbpassword>@ds151614.mlab.com:51614/user_data
host =  "ds151614.mlab"
port = "51614"
db_name="userdata"
user_name = "admin"
pasword = "admin1"
def connect():
    mongoengine.connect(db_name,host=host,user_name=user_name,pasword=pasword)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())