from django.contrib import admin
from .models import *

admin.site.register(Recipe)
admin.site.register(Content)
admin.site.register(Step)
admin.site.register(Ingredient)
