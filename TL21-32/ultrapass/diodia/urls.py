from django.urls import path
from . import views
#URLConf
urlpatters = [
    path(" ", views.say_hello, name="index")
]