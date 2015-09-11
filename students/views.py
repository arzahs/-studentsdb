# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext
# Create your views here.
def home(request):
	students = (
		{'id': 1,
		'first_name': 'Сергей',
		'last_name':'Нелепа',
		'ticket':1,
		'image':'static/img/me2.jpg'
		},
		{'id': 2,
		'first_name': 'Сергей',
		'last_name':'Нелепа',
		'ticket':11,
		'image':'static/img/me2.jpg'
		},
		{'id': 3,
		'first_name': 'Сергей',
		'last_name':'Нелепа',
		'ticket':12,
		'image':'static/img/me2.jpg'
		},
	)
	return render(request, 'students/students_list.html', {"students": students})

def students_add(request):
	return HttpResponse('here will be form students')
def students_edit(request, sid):
	return HttpResponse('here will be form students %s' % sid)

def groups_list(request):
	return HttpResponse('here will be form group')

def journal(request):
	return HttpResponse('here will be journal')