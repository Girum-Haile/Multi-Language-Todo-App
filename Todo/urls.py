from django.urls import path
from .views import home, add_todo, delete_todo, edit

app_name = 'Todo'

urlpatterns = [
    path('', home, name='home'),
    path('add_todo/', add_todo, name="add_todo"),
    path('delete_todo/<int:todo_id>/', delete_todo, name="delete_todo"),
    path('edit/<int:todo_id>/', edit, name="edit")
]
