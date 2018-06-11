# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView
from .models import Link, Vote

# Create your views here.
class LinkListView(ListView):
    model = Link
    queryset = Link.with_votes.all()#instead of default Link.objects.all()
