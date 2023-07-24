# program to Convert from Python to JSON
import json

demo = {
    "id": 101,
    "name": "surya",
    "age": 25
}
print(demo)
print(type(demo))
# converting into JSON
demo1 = json.dumps(demo)
# displaying in JSON string
print(demo1)
print(type(demo1))
