from django.db import models


class IngredientCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(IngredientCategory, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class IngredientAttribute(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)
    attribute = models.ForeignKey(IngredientAttribute, on_delete=models.CASCADE, null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.quantity} {self.ingredient.name}"

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    prep_time = models.PositiveIntegerField()
    cook_time = models.PositiveIntegerField()
    servings = models.PositiveIntegerField()
    directions = models.TextField()
    ingredients = models.ForeignKey(RecipeIngredient, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
