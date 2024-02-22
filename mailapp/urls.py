from . import views
from django.urls import path


urlpatterns=[
    path('m/',views.send_emails,name='send_emails'),
]