from django.urls import path
from .views import *


urlpatterns = [
    path('', recipes_list, name='recipes_list'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
]
