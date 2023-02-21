from django.urls import path
from .views import TaskView, TaskCreate, TaskUpdate, TaskDelete, TaskDetail
from . import views

urlpatterns = [

    path('TaskView/', TaskView.as_view(), name='items'),
    path('TaskCreate/', TaskCreate.as_view(), name='created_items'),
    path('TaskUpdate/<int:pk>/', TaskUpdate.as_view(), name='update_items'),
    path('TaskDelete/<int:pk>/', TaskDelete.as_view(), name='delete_items'),
    path('TaskDetail/<int:pk>/', TaskDetail.as_view(), name='detail_view'),
    path('login', views.login_fun, name='login'),
    path('register',views.register_fun, name='register'),

]
