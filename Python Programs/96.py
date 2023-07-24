# program to convert python objects into JSON strings
import json

print(json.dumps({"id": 101, "name": "surya"}))  # dictionary
print(json.dumps(["klu", "cse"]))  # list
print(json.dumps(("klu", "cse")))  # tuple
print(json.dumps("klu"))  # string
print(json.dumps(13))  # int
print(json.dumps(13.45))  # float
print(json.dumps(True))  # boolean
print(json.dumps(False))  # boolean
print(json.dumps(None))  # None
