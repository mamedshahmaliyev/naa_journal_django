
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='teacher_index'),
    path('view/<int:teacher_id>/', views.view, name='teacher_view'),
    path('edit/<int:teacher_id>/', views.edit, name='teacher_edit'),
    path('add/', views.add, name='teacher_add'),
]