# program to parse JSON - Convert from JSON to Python
import json

demo = '{"id": 101, "name": "surya", "salary": 12350.00, "gender": "male", "101": 10}'
print(type(demo))
demo1 = json.loads(demo)
print(type(demo1))
print(demo1)
print(demo1['id'])
print(demo1['name'])
print(demo1['101'])
