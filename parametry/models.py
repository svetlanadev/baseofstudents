# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models


class Groupofstudents(models.Model):
	name = models.CharField(max_length=128, unique=True, verbose_name=u'Групи')


	class Meta:
		verbose_name_plural = 'Groupofstudents'

	def __unicode__(self):
		return self.name


