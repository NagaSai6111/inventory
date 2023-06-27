from django.urls import path
from .views import login, register, dashboard
from . import views
urlpatterns = [
    path('', login , name="login"),
    path('register/', register, name="register"),
    path('dashboard/',dashboard, name="dashboard" )
     
]
