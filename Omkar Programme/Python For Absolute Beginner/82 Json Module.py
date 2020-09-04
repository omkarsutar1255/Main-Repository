import json
data = '{"var1":"omkar", "var2":56}'
parsed = json.loads(data)         # convert json in python
print(type(parsed))
print(parsed['var1'])

# task 1 = json.load?           # convert json 'file' into python

data2 = {
    "channelname":"starplus",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge" : ('roti', 540),
    "isbad":False
}
jscomp = json.dumps(data2)       #convert python into json
print(jscomp)

# task 2 = what is sort_keys parameter in dumps
info = {
    "name": "omkar",
    "age": "22",
    "married": "False",
    "divorced": "False",
    "childre": "none",
    "pet": "cat",
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
print(json.dumps(info, indent=4, sort_keys=True))