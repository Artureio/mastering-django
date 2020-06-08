from django.urls import path
from . import views

app_name = 'hello'
urlpatterns = [
    path('<str:name>/', views.greet, name='greet'),
    path('', views.askName, name='ask'),
]
