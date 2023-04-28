import json

import json

with open('data/delish_recipes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

maxrecipe = 0
maxingredient = 0
maxstep = 0
maxcontent = 0

for recipe in data:
    if maxrecipe < len(recipe['name']):
        maxrecipe = len(recipe['name'])
    for ingredient in recipe['ingredients']:
        if maxingredient < len(ingredient):
            maxingredient = len(ingredient)
    for step in recipe['steps']:
        if maxstep < len(step):
            maxstep = len(step)
    for content in recipe['content']:
        if maxcontent < len(content):
            maxcontent = len(content)

print("maxrecipe: " + str(maxrecipe))
print("maxingredient: " + str(maxingredient))
print("maxstep: " + str(maxstep))
print("maxcontent: " + str(maxcontent))
