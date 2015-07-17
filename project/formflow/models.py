from django.db import models

# Create your models here.

FLOW_ACTIONS = (
	('NONE', 'NONE'),
	('NEXT','NEXT'),
	('PREV','PREV'),
	('SUMMARY', 'SUMMARY'),
	('SEND', 'SEND'),
)
class Flow(models.Model):
	name = models.CharField(max_length=64)
	currentForm = models.OneToOneField('Form', related_name='flow_currentForm', null=True, blank=True)
	action = models.CharField(max_length=16, choices=FLOW_ACTIONS, default='NONE')
	
	def __unicode__(self):
		return self.name

FORM_TYPES = (
	('SIMPLE', 'SIMPLE'),
	('ARRAY', 'ARRAY'),
)
class Form(models.Model):
	name = models.CharField(max_length=64)
	type = models.CharField(max_length=16, choices=FORM_TYPES)
	flow = models.ForeignKey(Flow)
	
	def __unicode__(self):
		return str(self.flow) + ':' + self.name

FIELD_TYPES = (
	('DATE', 'DATE'),
	('EMAIL', 'EMAIL'),
	('NAME', 'NAME'),
)
class Field(models.Model):
	name = models.CharField(max_length=64)
	type = models.CharField(max_length=16, choices=FIELD_TYPES)
	form = models.ForeignKey(Form)
	
	def __unicode__(self):
		return str(self.form) + ':' + self.name
