import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds151614.mlab.com:51614/user_data

host = "ds151614.mlab.com"
port = 51614
db_name = "user_data"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json