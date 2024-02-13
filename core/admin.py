from django.contrib import admin

from .models import User,Task, Category

admin.site.register(User)
admin.site.register(Task)
admin.site.register(Category)

# Register your models here.
