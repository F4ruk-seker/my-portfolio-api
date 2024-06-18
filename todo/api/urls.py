from django.urls import path, include
from todo.api import views


app_name = "todo"

urlpatterns = [
    path('', views.AllToDoListView.as_view(), name='todos'),
    path('add/todo/', views.ToDoCreateView.as_view(), name='todos'),
    path('add/category/', views.ToDoCategoryCreateView.as_view(), name='todo_category_create'),
    path('category/<pk>', views.ToDoCategoryRetrieveUpdateDestroyView.as_view(), name='todo_category'),
    path('<pk>', views.ToDoRetrieveUpdateDestroyView.as_view(), name='todos'),
]


