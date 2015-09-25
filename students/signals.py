# -*- coding: utf-8 -*-
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .models import Student
import logging
@receiver(post_save, sender=Student)
def log_student_updated_signal(sender, **kwargs):
	"""Log student update/create signals into file"""
	logger = logging.getLogger(__name__)
	student = kwargs['instance']
	if kwargs['created']:
		logger.info(u'Student created: %s %s (ID: %d)', student.first_name, 
			student.last_name, student.id )
	else:
		logger.info(u'Student updated: %s %s (ID: %d)', student.first_name, 
			student.last_name, student.id )

@receiver(post_delete, sender=Student)
def log_student_updated_signal(sender, **kwargs):
	"""Log student delete signals into file"""
	logger = logging.getLogger(__name__)
	student = kwargs['instance']
	logger.info(u'Student deleted: %s %s (ID: %d)', student.first_name, 
			student.last_name, student.id )


