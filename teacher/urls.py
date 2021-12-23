from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_teachers, name='teacher-list'),
    path('<int:teacher_id>/details/', views.get_teacher, name='teacher-detail'),
    path('create/', views.create_teachers, name='create-teacher'),
]
