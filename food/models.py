from django.db import models

class Ingredient(models.Model):
    text = models.CharField(max_length=100)
    def __str__(self):
        return self.text

class Step(models.Model):
    text = models.CharField(max_length=100)
    def __str__(self):
        return self.text

class Content(models.Model):
    text = models.CharField(max_length=100)
    def __str__(self):
        return self.text

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    contents = models.ForeignKey(Content, on_delete=models.CASCADE)
    steps = models.ForeignKey(Step, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
