from django.conf.urls import url, include
from email_app import views

urlpatterns = [
url(r'^home/$', views.home, name = 'home')
]
