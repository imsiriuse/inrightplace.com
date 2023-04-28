from django.shortcuts import render
from .models import Recipe
from django.shortcuts import get_object_or_404

def recipes_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes_list.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    steps = recipe.steps.all()
    ingredients = recipe.ingredients.all()
    contents = recipe.contents.all()

    context = {
        'recipe': recipe,
        'steps': steps,
        'ingredients': ingredients,
        'contents': contents,
    }

    return render(request, 'recipe_detail.html', context)
