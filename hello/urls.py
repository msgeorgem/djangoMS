from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'hello'
urlpatterns = [
    path('', TemplateView.as_view(template_name='hello/main.html')),
    path('cookie', views.cookie),
    path('sessfun', views.sessfun),
]