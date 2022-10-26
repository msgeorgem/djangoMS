from django.urls import path, include
from django.views.generic import TemplateView
from .views import SignUpView

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view()),
    path('', views.HomeView.as_view(), name='index'),
    path("signup/", SignUpView.as_view(), name="signup"),

]