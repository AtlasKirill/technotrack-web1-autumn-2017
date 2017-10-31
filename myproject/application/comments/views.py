# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.views.generic import UpdateView
from comments.models import Comment

# Create your views here.



class EditComment(UpdateView):
    template_name = 'blog/edit_comment.html'
    model = Comment
    fields = ('text',)

    def get_queryset(self):
        return super(EditComment, self).get_queryset().filter(
            author=self.request.user,
        )

    def get_success_url(self):
        return reverse('core:mainpg')