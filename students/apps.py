# -*- coding: utf-8 -*-

from django.apps import AppConfig

class StudentsAppConfig(AppConfig):
	name = 'students'
	verbose_name=u'Database of students'
	def ready(self):
		from students import signals
