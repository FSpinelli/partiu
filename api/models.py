# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	active = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Event(models.Model):
	name = models.CharField(max_length=200, null=True)
	category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)
	description = models.TextField(null=True, blank=True)
	address = models.CharField(max_length=200, null=True)
	location = models.CharField(max_length=200, null=True)
	coordinate = models.CharField(max_length=200, null=True)
	date = models.DateField(null=True)
	start_time = models.TimeField(null=True)
	end_time = models.TimeField(null=True)
	image = models.ImageField(upload_to="%Y/%m/%d/")
	active = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Favorite(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
	event = models.ForeignKey(Event, null=True, on_delete=models.PROTECT)

	def __str__(self):
		return self.user.username