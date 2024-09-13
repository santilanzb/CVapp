from django.ruls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

