from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^welcome/$', views.welcome, name='welcome'),
    url(r'^sign_in/$', views.sign_in, name='sign_in'),
    url(r'^sign_up/$', views.SignUp.as_view(), name='sign_up'),
    url(r'^sign_up/$', views.SignUp.as_view(), name='group'),

]
