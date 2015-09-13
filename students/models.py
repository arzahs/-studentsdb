from django.db import models

# Create your models here.
class  Student(models.Model):
	"""Student Model"""
			
	first_name =models.CharField(max_length=256, blank=False, verbose_name='Name')
	last_name = models.CharField(max_length=256, blank=False, verbose_name='Last Name')
	middle_name = models.CharField(max_length=256, blank=True, verbose_name='Middle Name', default='')
	birthday = models.DateField(blank=False, verbose_name='Birthday')
	#photo = models.ImageField(blank=True, verbose_name='Photo')
	ticket = models.CharField(max_length=256, blank=False, verbose_name='Ticket')
	notes = models.TextField(blank=True, verbose_name='Notes', default='')

	def __str__(self):
		return u'%s %s' % (self.first_name, self.last_name)