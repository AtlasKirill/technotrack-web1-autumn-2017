# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import resolve_url
from django.views.generic import FormView

from comments.models import Comment
from django.views.generic.base import TemplateView
from blog.models import Blog, Post
from core.forms import UserRegistration



class HomePageView(TemplateView):
    template_name = "core/base.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_articles'] = Blog.objects.order_by('-createdata')[:3]
        context['blog_count'] = Blog.objects.all().count()
        context['post_count'] = Post.objects.all().count()
        context['comment_count'] = Comment.objects.all().count()
        return context

class RegisterFormView(FormView):
    form_class = UserRegistration
    template_name = "core/signup.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('core:mainpg')