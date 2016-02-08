from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /main/
    url(r'^$', views.index, name='index'),
]