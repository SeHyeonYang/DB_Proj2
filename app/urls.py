from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^welcome/$', views.welcome, name='welcome'),
    url(r'^sign_in/$', views.sign_in, name='sign_in'),
    url(r'^lecture/add$', views.LectureAdd.as_view(), name='lecture_add'),
    url(r'^lecture/all$', views.lecture_all, name='lecture_all'),
    url(r'^sign_up/$', views.SignUp.as_view(), name='sign_up'),
    url(r'^group_home/$', views.group_home, name='group_home'),
    url(r'^id_check/$', views.id_check, name='id_check'),
    url(r'^total_article/$', views.total_article, name='total_article'),
    url(r'^my_page/(?P<menu>[\w]+)/$', views.my_page, name='my_page'),
    url(r'^group_create/$',views.group_creat,name ='group_create')
]
