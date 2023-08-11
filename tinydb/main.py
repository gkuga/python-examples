import tinydb


class Person():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


db = tinydb.TinyDB('db.json')
table = db.table('sample')
table.upsert(tinydb.table.Document(
    {'name': 'John', 'age': 22, 'sex': 'male'},
    doc_id=0),
)
table.upsert(tinydb.table.Document(
    {'name': 'Bob', 'age': 20},
    doc_id=1),
)
table.upsert(tinydb.table.Document(
    {'name': 'Bob', 'age': 20},
    doc_id='abc'), # this is a bug
)
item = table.get(None, 'abc') # this will be error
p = Person(item['name'], item['age'], 'sex')
print(item.get('status', 'private'))
