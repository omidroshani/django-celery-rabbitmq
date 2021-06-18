from django.urls import path
from .views import sample_request
from django.conf.urls import url



urlpatterns = [
    url(r'sample/', sample_request, name='sample_request')
]