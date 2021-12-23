from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_students, name='students-list'),
    path('<int:student_id>/details/', views.get_student,
         name='student-detail'),
    path('create/', views.create_students, name='create-student'),
]
