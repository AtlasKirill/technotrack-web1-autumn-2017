from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from blog.views import *
from comments.views import EditComment

urlpatterns = [
    url(r'^$', BlogList.as_view(), name='blogspage'),
    url(r'^(?P<id>\d+)$', posts_list, name='blogsview'),
    url(r'^(?P<id_2>\d+)/(?P<id_1>\d+)$', post_page, name='onepost'),
    url(r'^blog/(?P<id_2>\d+)/(?P<pk>\d+)/edit/$', EditPost.as_view(), name="editpost"),
    url(r'^blog/(?P<id_2>\d+)/(?P<pk>\d+)/edit_comment/$', EditComment.as_view(), name="editcomment"),
    url(r'^new/$', login_required(New_Post.as_view()), name="post_creation"),
]
