import json
import pymongo

# conn_str provides the MongoClient with the connection link needed for the client to connect to our MongoDB Atlas cluster
conn_str = "mongodb+srv://demo:aqnbBggYWFKl8aO8@cluster0.crvoq.mongodb.net/Cluster0?retryWrites=true&w=majority"

# client provides us with the ability to perform crud functions in our database
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

# specify what database and collection we are accessing
db = client['Notable_Health']
collection = db['Physicians']

def getAllDoctors(event,context):
    physicians = collection.find({})
    physiciansDict = {}

    # collection.find({}) returns a cursor object
    # which is iterable, allowing me to create an object
    # with the physicians ID as the key, with their info as the value
    # although I do realize the ineffeciency of this approach
    # it was implemented in the interest of time, given more time
    # I would find a more effecient way to implement this
    for inventory in physicians:
        physiciansDict[inventory['_id']] = inventory

    body = {
        "message": "Successfully retrieved all Physicians",
        "physicians": physiciansDict
    }

    # debugging with this print statement
    # print(physicians['cursor'], "BODY")

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def getDoctorsAppointments(event, context):

    # debugging with this print statement
    # print(event)
    physicianId = event['pathParameters']['physicianId']
    date = event['pathParameters']['date']

    physician = collection.find_one({"_id": physicianId})
    appointments = physician['appointments']
    dateAppointments = appointments[date]

    body = {
        "message": f"Successfully retrieved appointments on {date}.",
        "appointments": dateAppointments
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

# my plan for the delete appointment function was to utilize
# physician ID from the path, and the date, time, and patientId
# from query parameters, in order to update the document under
# the appropriate date, and time, removing the user that is specified
def deleteAppointment(event, context):
    physicianId = event['pathParameters']['physicianId']

# my plan for the add appointment function was to utilize
# physician ID from the path, and the date, time, and patientId
# from query parameters, in order to create the appointment at the
# specified date and time, checking to make sure that there were a maximum of 3
# patients under the give time
def addNewAppointment(event, context):
    pass

# The document shape, each document being a physician
# the _id is the physicianId
# {
#     "_id":"1",
#     "physicianName":"Bob Sir",
#     "appointments":{
#         "02/07/2022":{
#             "8:15":{
#                 "1":{
#                     "patientName":"Tom"
#                 },
#                 "2":{
#                     "patientName":"Phil"
#                 },
#                 "3":{
#                     "patientName":"John"
#                 }
#             }
#         }
#     }
# }
