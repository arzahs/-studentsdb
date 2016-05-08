from django.test import TestCase
from django.http import HttpRequest
from students.models import Student, Group
from students.util import get_current_group, paginate
from datetime import datetime


class UtilsTestCase(TestCase):

    def setUp(self):
        # create set users and groups of DATABASES
        group1, created = Group.objects.get_or_create(
                                                id=1,
                                                title="Group1")
        group2, created = Group.objects.get_or_create(
                                                id=2,
                                                title="Group2")

        student1, created = Student.objects.get_or_create(id=1,
                                                          first_name="Sergey",
                                                          last_name="Nelepa",
                                                          birthday=datetime.now(),
                                                          ticket='1234'
                                                          )
        group1.leader = student1
        group1.save()


    def test_get_current_group(self):
        request = HttpRequest()
        request.COOKIES['current_group'] = ''
        self.assertEquals(None, get_current_group(request))
        request.COOKIES['current_group'] = '123245'
        self.assertEquals(None, get_current_group(request))
        group = Group.objects.filter(title='Group1')[0]
        request.COOKIES['current_group'] = str(group.id)
        self.assertEquals(group, get_current_group(request))
        group = Group.objects.filter(title='Group2')[0]
        request.COOKIES['current_group'] = str(group.id)
        self.assertEquals(group, get_current_group(request))

    def test_paginate(self):
        context = { }
        request = HttpRequest()
        pass
