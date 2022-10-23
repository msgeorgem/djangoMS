from django.urls import path, include
from django.views.generic import TemplateView
from .views import SignUpView

from . import views

app_name = 'hello'
urlpatterns = [
    path('', views.HomeView.as_view()),
    path("signup/", SignUpView.as_view(), name="signup"),

]