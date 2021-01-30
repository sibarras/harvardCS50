from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("samuel", views.samuel, name="samuel"),
    path("luz", views.luz, name="luz"),
    path("<str:name>", views.greet, name='greet')

]
