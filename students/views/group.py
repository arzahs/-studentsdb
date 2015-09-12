# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext

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