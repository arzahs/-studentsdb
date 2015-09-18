# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext
from students.models import Group
from django.core.paginator  import Paginator, EmptyPage, PageNotAnInteger
def groups_list(request):
	groups = Group.objects.all()
	paginator = Paginator(groups, 5)
	page = request.GET.get('page')
	try:
		groups = paginator.page(page)
	except PageNotAnInteger:
		groups = paginator.page(1)
	except EmptyPage:
		groups = paginator.page(paginator.num_pages)
	return render(request, 'students/groups_list.html', {"groups": groups})

def groups_edit(request, sid):
	return HttpResponse('group edit %s'% sid)

def groups_delete(request, sid):
	return HttpResponse('group delete %s'% sid)