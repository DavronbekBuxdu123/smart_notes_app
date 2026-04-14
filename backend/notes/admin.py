from django.contrib import admin
from .models import Category,Note,Tag
# Register your models here.
admin.site.register(Category)
admin.site.register(Note)
admin.site.register(Tag)