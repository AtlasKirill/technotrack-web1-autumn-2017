# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from django.shortcuts import render

from django.shortcuts import render

# Create your views here.

def main_page(request, name=None):

    return render(request,'main_page.html',{'name':name})

