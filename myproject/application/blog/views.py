# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse

from django.http import Http404
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from .models import Blog, Post


# Create your views here.


def post_page(request, id_2=None, id_1=None):
    blog = get_object_or_404(Blog.objects, id=id_2)
    post = get_object_or_404(Post.objects, id=id_1)
    if (post.blog.id == blog.id):
        return render(request, 'blog/post_page.html', {'post': post})
    else:
        raise Http404


def posts_list(request, id=None):
    blog = get_object_or_404(Blog.objects, id=id)
    return render(request, 'blog/posts_list.html', {'blog': blog})


class BlogList(ListView):
    template_name = "blog/blogpage.html"
    context_object_name = 'blog'
    model = Blog


class EditPost(UpdateView):
    template_name = 'blog/edit_post.html'
    model = Post
    fields = 'postname', 'text'

    def get_queryset(self):
        return super(EditPost, self).get_queryset().filter(
            author=self.request.user,
            blog__pk=self.kwargs['id_2']
        )

    def get_success_url(self):
        return reverse('core:mainpg')


class New_Post(CreateView):
    template_name = 'blog/new_post.html'
    model = Post
    fields = 'postname', 'text', 'blog'

    def get_success_url(self):
        return reverse('core:mainpg')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(New_Post, self).form_valid(form)

