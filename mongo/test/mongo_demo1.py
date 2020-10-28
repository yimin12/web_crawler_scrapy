import pymongo

# Connect mongodb server
client = pymongo.MongoClient()
# decide which database of sever to connect
person = client.person
# decide which collections of database to connect
student = person.student
# manipulate database
result = student.find()
# print
# for r in result:
#     print(r)
#
# print(result.next())
# print(result.next())
# print(result.next())

# filter condition
result_f = student.find({"country":"蜀国"})
result_f1 = student.find().sort("age",1)
result_f2 = student.find().sort("age",pymongo.DESCENDING)
result_count = student.find().count()

# paging
result_p = student.find().limit(6).skip(6)

# add data
data = {"name":"Theshy", "age":18}
# student.insert_one(data)

# remove data
# student.delete_one(data)

# update data
data = {"name":"Theshy"}
# for r in result_p:
#     print(r)
# print(result_count)

result_update = student.find_one(data)
print(result_update)
result_update["age"]=20
student.update_one(data,{"$set":result_update})