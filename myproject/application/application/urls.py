# -*- coding: utf-8 -*-
"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core.views import main_page
from core.views import all_blogs
from core.views import all_post_in_blog
from core.views import certain_post

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/$', main_page),
    url(r'^blog/$', all_blogs),
    url(r'^blog/(?P<name>\d+)/$',all_post_in_blog ),
    url(r'^blog/(?P<name1>\d+)/post/(?P<name2>\d+)/$', certain_post),
]
