import json

# created a Python object (dict):
x = {
  "name": "Jenna",
  "age": 30,
  "city": "Melbourne"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)