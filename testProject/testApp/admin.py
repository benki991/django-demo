from django.contrib import admin
from .models import TestModel, user_login
# Register your models here.
admin.site.register(TestModel)
admin.site.register(user_login)