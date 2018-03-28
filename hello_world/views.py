# encoding: utf-8
from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'hello_world/index.html')
