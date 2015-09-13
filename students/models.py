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
	student_group = models.ForeignKey('Group',
		verbose_name='Group', 
		blank=False, null=True, on_delete=models.PROTECT)
	notes = models.TextField(blank=True, verbose_name='Notes', default='')

	def __str__(self):
		return u'%s %s' % (self.first_name, self.last_name)

class Group(models.Model):
	"""docstring for Group"""
	title =models.CharField(max_length=256, blank=False, verbose_name='Title')
	notes = models.TextField(blank=True, verbose_name='Notes', default='')	
	leader = models.OneToOneField('Student',
	verbose_name='Leader',
	blank=True,
	null=True,
	on_delete = models.SET_NULL)
	def __str__(self):
		return u'%s' % (self.title)