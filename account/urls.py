from django.urls import path
from . import views
from .views import Register

urlpatterns = [
    #path("register/", Register.as_view(), name = 'register'),
   # path("login/", Login.as_view(), name = "login"),
]
