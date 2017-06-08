from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^welcome/$', views.welcome, name='welcome'),
    url(r'^leave/$', views.leave, name='leave'),
    url(r'^sign_in/$', views.sign_in, name='sign_in'),
    url(r'^lecture/add/$', views.LectureAdd.as_view(), name='lecture_add'),
    url(r'^lecture/all/$', views.LectureAll.as_view(), name='lecture_all'),
    url(r'^lecture_check/$', views.lecture_check, name='lecture_check'),
    url(r'^lecture/detail/$', views.LectureDetail.as_view(), name='lecture_detail'),
    url(r'^lecture/(?P<lecture>.*)/section/add/$', views.SectionAdd.as_view(), name='section_add'),
    url(r'^lecture/(?P<category>[\w]+)/$', views.lecture_category, name='lecture_category'),
    url(r'^sign_up/$', views.SignUp.as_view(), name='sign_up'),
    url(r'^sign_out/$', views.sign_out, name='sign_out'),
    url(r'^group_home/$', views.group_home, name='group_home'),
    url(r'^id_check/$', views.id_check, name='id_check'),
    url(r'^article/(?P<pk>[\d]+)/$', views.info_article, name='article'),
    url(r'^article/(?P<option>[\w]+)/$', views.article, name='article'),
    url(r'^my_page/(?P<menu>[\w]+)/$', views.my_page, name='my_page'),
    url(r'^group_create/$',views.group_create,name ='group_create'),
    url(r'^group_private/$',views.group_private,name ='group_private'),
]
