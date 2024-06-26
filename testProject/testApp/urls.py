from . import views
from django.urls import re_path

urlpatterns = (
    re_path(r'^$', views.home, name="home"),
    re_path(r'^tailwind$', views.tailwindSample, name="tailwind"),
    re_path(r'^save$', views.save, name="save"),
    re_path(r'^del$', views.delUser, name="delUser"),
    re_path(r'^update$', views.update, name="update"),
    re_path(r'^login$', views.login, name="login"),
    re_path(r'^login_user$', views.login_user, name="login_user"),
)
