# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from django.shortcuts import render

from django.shortcuts import render


# Create your views here.

def main_page(request, name=None):
    return render(request, 'main_page.html')


def all_blogs(request):
    return render(request, 'all_blogs.html')


def all_blogs(request):
    return render(request, 'all_blogs.html')


def all_post_in_blog(request, name=None):
    return render(request, 'all_post_in_blog.html', {'name': name})


def certain_post(request, name1=None, name2=None):
    return render(request, 'certain_post.html', {'name1': name1, 'name2': name2})
