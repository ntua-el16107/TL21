from django.urls import path
from . import views
#URLConf
urlpatters = [
    path('hello/', views.say_hello)
]