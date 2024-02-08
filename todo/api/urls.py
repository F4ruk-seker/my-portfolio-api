from django.urls import path, include
from todo.api import views


app_name = "todo"

urlpatterns = [
    path('', views.AllToDoListView.as_view(), name='todos'),
    path('add/', views.ToDoCreateView.as_view(), name='todos'),
    path('<pk>', views.ToDoRetrieveUpdateDestroyView.as_view(), name='todos'),
]


