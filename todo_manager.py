from pymongo import MongoClient

host = "localhost"
port = 27017
database = "mongo_task"
username = "django"
password = "1"

client = MongoClient(host, port)
db = client[database]
collection = db["tasks"]


def create_task(task):
    collection.insert_one(task)


def get_tasks():
    tasks = collection.find()
    return list(tasks)


def update_task(task_id, new_task):
    collection.update_one({"_id": task_id}, {"$set": new_task})


def delete_task(task_id):
    collection.delete_one({"_id": task_id})
