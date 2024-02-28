from pymongo import MongoClient
from pprint import pprint
from bson import ObjectId
 
# Connect to the MongoDB cluster
client = MongoClient("mongodb+srv://DB1Admin:<password>@cluster0.pzvdcy0.mongodb.net/")

# Specify the database and collection names
db_name = "leisure_centre"
collection_name = "Course"
 
# Get the collection object
mongo_db = client[db_name]
mongo_coll = mongo_db[collection_name]

# docs = mongo_coll.find()
# for aDoc in docs:
#     pprint(aDoc)
    
#


# dbMongoClient = client["leisure_centre"]['Lessons']


# print("\n Add single document \n")
# addDoc = dbMongoClient.insert_one ({"CourseID": 500,"MemberID": 190})
#  print(addDoc.inserted_id)

# Updates a single document

# print("\nUpdate document\n")
# updateDoc = dbMongoClient.update_one({'CourseID': 3}, {'$set':{"MemberID":230}})
# print(updateDoc.modified_count)



# dbMongoClient = client["leisure_centre"]['Lessons']



#updates multiple documents

# print("\nUpdate Multiple documents\n")
#updateDocs = dbMongoClient.update_many({'MemberID': 15}, {'$set':{"CourseID":2111}})
# print(f"The number of updated documents: {updateDocs.modified_count}")




# print("\ninsert Many document\n")
# documents = [
# {'CourseID': 51, 'MemberID': 55 },
# {'CourseID': 52, 'MemberID': 56},
# {'CourseID': 53, 'MemberID': 57},
# {'CourseID': 54, 'MemberID': 58}
# ]

# addDocs = dbMongoClient.insert_many(documents)
# print(addDocs.inserted_ids)




# dbMongoClient = client["leisure_centre"]['Members']

# print("\nAdding Member document\n")

#Adds a member document

# addDoc = dbMongoClient.insert_one({'MemberID':51 ,'Firstname': 'John', 'Surname': 'Doe', 'DOB': '10/10/2010'})
# print(addDoc.inserted_id)



# 2. Where courseID is equals to a number above 5 and the lesson time is in the morning or afternoon.

# dbMongoClient = client["leisure_centre"]['Lessons']

# belowDocs = dbMongoClient.find({
#     "$and": [
#         {"CourseID": {"$gt": 5}},
#         {"$or": [
#             {"LessonTime": {"$regex": "^[0-9]{2}:[0-9]{2} (AM|PM)$"}},
#             {"LessonTime": {"$regex": "^[0-9]{2}:[0-9]{2} (AM|PM)$"}}
#         ]}
#     ]
# })

# for doc in belowDocs:
#     pprint(doc)

                         
##################Start Time######################

# dbMongoClient = client["leisure_centre"]['Course']

# result_b1 = dbMongoClient.find().sort("startDate")
# for doc in result_b1:
#     pprint( doc)

#################Order by MemberID######################

# dbMongoClient = client["leisure_centre"]['Members']

# result_b2 = dbMongoClient.find().sort("MemberID")

# for doc in result_b2:
#     pprint( doc)



# 1. Members table, change the addresses of any three members.

# collection_name = dbMongoClient = client["leisure_centre"]['Members']

# id1 = ObjectId('65b0058401ddecfa2fbfe5d5')
# id2 = ObjectId('65b0058401ddecfa2fbfe5e2')
# id3 = ObjectId('65b0058401ddecfa2fbfe5f4')

# updateMembers = collection_name.update_many(
#     {"_id": {"$in": [id1, id2, id3]}},
#     {"$set": {"Address": "Room 1"}}
# )

# print(f"The number of updated documents: {updateMembers.modified_count}")




# 2. Course table, change the startDate and lesson time for three of the sessions.

# dbMongoClient = client["leisure_centre"]['Course']

# updateCourse = dbMongoClient.update_many(
#  {"CourseID": {"$in": [1, 2, 3]}},
#  {"$set": {"StartDate": "2024-1-20", "LessonTime": "16:30 PM"}})



# dbMongoClient = client["leisure_centre"]['Course']
# min_lesson_id = dbMongoClient.find_one ({}, sort=[("CourseID", 1)])["CourseID"]

# print("Exercise D1 - Min LessonID:", min_lesson_id)


# dbMongoClient = client["leisure_centre"]['Members']
# max_members_id = dbMongoClient.find_one ({}, sort=[("MemberID", -1 )])["MemberID"]

# print("Exercise D1 - Max MemberID:", max_members_id)

# dbMongoClient = client["leisure_centre"]['Members']

# total_members_id = dbMongoClient.count_documents({})
# print("Total Members:", total_members_id)

# dbMongoClient = client["leisure_centre"]['Course']

# total_sessions=dbMongoClient.count_documents({})
# print("Total Sessions:", total_sessions)

## F. WILDCARD queries (regex operator)

# dbMongoClient = client["leisure_centre"]['Members']
# member_id = dbMongoClient.find({"Surname": {"$regex":"^A"}})
# for doc in member_id:
#  print("Last name:", doc)