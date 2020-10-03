from django.urls import path
from .views import home, add_todo, edit_todo, delete_todo

app_name = 'Todo'

urlpatterns = [
    path('', home, name='home'),
    path('add_todo/', add_todo, name="add_todo"),
    path('edit_todo/<int:todo_id>/', edit_todo, name="edit_todo"),
    path('delete_todo/<int:todo_id>/', delete_todo),

]
