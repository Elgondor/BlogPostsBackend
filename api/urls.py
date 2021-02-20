from django.urls import path, re_path
from django.conf.urls import url
from .views import ListPosts

app_name = 'api'

urlpatterns = [
    # url(r'^posts/$', ListPosts.as_view()),
    # url(r'^posts/<int:tags>$', ListPosts.as_view())
    # re_path(r'^posts/(?P<tags>[0-9]{1})/$', ListPosts.as_view()),
    path('posts/', ListPosts.as_view(), name='posts'),
]