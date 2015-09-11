from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext
# Create your views here.
def test(request):
	return render(request, 'students/students_list.html', {})