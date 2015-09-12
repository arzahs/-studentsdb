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
	groups = ({'name':'mf111'}, {'name':'mf112'}, {'name':'mf113'})
	return render(request, 'students/students_list.html', {"students": students, "groups": groups})

def students_add(request):
	return HttpResponse('here will be form students')

def students_edit(request, sid):
	return HttpResponse('here will be form students %s' % sid)

def students_visiting(request, sid):
	return HttpResponse('visiting %s' % sid)

def students_delete(request, sid):
	return HttpResponse('delete %s' % sid)

def groups_list(request):
	groups = ({
		'id':1,
		'name':'mf131',
		'steward': { 'id' : 1, 'name' : 'Нелепа Сергей'}
		},
		{
		'id':2,
		'name':'mf132',
		'steward': { 'id' : 2, 'name' : 'Сопельник Юлия'}
		},
		)
	return render(request, 'students/groups_list.html', {"groups": groups})
def groups_edit(request, sid):
	return HttpResponse('group edit %s'% sid)

def groups_delete(request, sid):
	return HttpResponse('group delete %s'% sid)

def journal(request):
	return HttpResponse('here will be journal')