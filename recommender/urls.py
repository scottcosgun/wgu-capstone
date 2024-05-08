from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('about', views.about, name='about')
]