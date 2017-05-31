from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^welcome/$', views.welcome, name='welcome'),
    url(r'^sign_in/$', views.sign_in, name='sign_in'),
    url(r'^sign_up/$', views.SignUp.as_view(), name='sign_up'),
    url(r'^sign_up/$', views.SignUp.as_view(), name='group'),
    url(r'^id_check/$', views.id_check, name='id_check'),
    url(r'^my_page/$', views.my_page, name='my_page'),
]
