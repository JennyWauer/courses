from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('destroy/<int:desc_id>', views.destroy),
    path('add_course', views.add_course),
]
