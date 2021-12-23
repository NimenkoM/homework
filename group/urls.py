from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_groups, name='group-list'),
    path('<int:group_id>/details/', views.get_group, name='group-detail'),
    path('create/', views.create_groups, name='create-group'),
]
