import pymongo
import django
print django.get_version()
from pymongo import MongoClient
client = MongoClient()
db = client['test-database']
person1 = {"name":"John Doe", "age":25}
person2 = {"name":"Jane Doe", "age":26, "dept": 115}
person1_id = db.employees.save(person1)
person2_id = db.employees.save(person2)
print person1_id
print person2_id
for employee in db.employees.find() :
    print employee
print db.employees.count()
db.employees.drop()