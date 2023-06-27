from django.contrib import admin
from .models import User
class Adminlogin(admin.ModelAdmin):
    list_display=('username','email','password')
admin.site.register(User,Adminlogin)