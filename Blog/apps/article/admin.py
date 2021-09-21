from django.contrib import admin
from .models import Category, SubCategory, Article
# Register your models here.


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Article)
