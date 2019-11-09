# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("Jeffrey Epstein did not kill himself")
    return render(request, 'posts/index.html')
