# program to demonstrate JSON Format and Order #demo is nested dictionary
import json

demo = {
    "zperson1": [
        {
            "first": "Nicole",
            "last": "Adelstein",
        }
    ],
    "aperson2": [
        {
            "first": "Pleuni",
            "last": "Pennings"
        }
    ],
    "cperson3": [
        {
            "first": "Rori",
            "last": "Rohlfs"
        }
    ]
}
print(json.dumps(demo))
print(json.dumps(demo, indent=5))
print(json.dumps(demo, indent=4, separators=(".", "=")))
print(json.dumps(demo, indent=5, sort_keys=True))  # sorting
# Execute each print statements by commenting other print statements
