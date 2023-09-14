from django.urls import path

from . import views
from django.views.generic import TemplateView
from core import views

app_name = "core"


urlpatterns = [
    path('faq/', views.FaqView.as_view(), name='faq'),
    path('contact/', views.ContactView.as_view(), name='contact'),

]