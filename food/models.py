from django.db import models

class Ingredient(models.Model):
    text = models.CharField(max_length=200)
    def __str__(self):
        return self.text

class Step(models.Model):
    text = models.CharField(max_length=1500)
    def __str__(self):
        return self.text

class Content(models.Model):
    text = models.CharField(max_length=100)
    def __str__(self):
        return self.text

class Recipe(models.Model):
    title = models.CharField(max_length=150)
    ingredients = models.ManyToManyField(Ingredient, related_name='ingredients')
    steps = models.ManyToManyField(Step, related_name='steps')
    contents = models.ManyToManyField(Content, related_name='contents')

    def __str__(self):
        return self.title
