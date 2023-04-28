import json

with open('data/delish_recipes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

fixture = []
recipes = []
ingredients = []
steps = []
contents = []

for inputrecipe in data:
    outputrecipe = {}

    outputrecipe['model'] = 'food.recipe'
    outputrecipe['pk'] = len(recipes) + 1
    outputrecipe['fields'] = {}
    outputrecipe['fields']['title'] = inputrecipe['name']
    outputrecipe['fields']['ingredients'] = []
    outputrecipe['fields']['steps'] = []
    outputrecipe['fields']['contents'] = []

    for ingredient in inputrecipe['ingredients']:
        outputingredient = {}
        outputingredient['model'] = 'food.ingredient'
        outputingredient['pk'] = len(ingredients) + 1
        outputingredient['fields'] = {}
        outputingredient['fields']['text'] = ingredient
        outputrecipe['fields']['ingredients'].append(outputingredient['pk'])
        ingredients.append(outputingredient)

    for step in inputrecipe['steps']:
        outputstep = {}
        outputstep['model'] = 'food.step'
        outputstep['pk'] = len(steps) + 1
        outputstep['fields'] = {}
        outputstep['fields']['text'] = step
        outputrecipe['fields']['steps'].append(outputstep['pk'])
        steps.append(outputstep)

    for content in inputrecipe['content']:
        outputcontent = {}
        outputcontent['model'] = 'food.content'
        outputcontent['pk'] = len(contents) + 1
        outputcontent['fields'] = {}
        outputcontent['fields']['text'] = content
        outputrecipe['fields']['contents'].append(outputcontent['pk'])
        contents.append(outputcontent)

    recipes.append(outputrecipe)

fixture.extend(recipes)
fixture.extend(ingredients)
fixture.extend(steps)
fixture.extend(contents)

with open('data/delish_recipes_export.json', 'w', encoding='utf-8') as f:
    json.dump(fixture, f, ensure_ascii=False, indent=4)
