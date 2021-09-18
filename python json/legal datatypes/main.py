import json

x = {
  "name": "Jenna",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("james","Aden"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))