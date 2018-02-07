# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# @csrf_exempt
context={}
class comment:
	"""docstring for ClassName"""
	name=""
	content=""
	def __init__(self, name, content):
		self.name = name
		self.content=content
		
comments=[];
# Create your views here.
def home_page(request):
    # render takes: (1) the request,
    #               (2) the name of the view to generate, and
    #               (3) a dictionary of name-value pairs of data to be
    #                   available to the view.

    return render(request, 'home.html', {})

def addcom(request):
	if 'username' in request.POST:
		comm=[str(request.POST['username']),str(request.POST['comments'])]
		comments.append(comm);
		context={}
		context['comments']=comments
		return render(request, 'showcomm.html', context)
	
	
	return render(request, 'addcomm.html',{})

def addP(request):
	return render(request, 'addcomm.html', {})

def showcom(request):
	context={}
	context['comments']=comments
	return render(request, 'showcomm.html', context)

























