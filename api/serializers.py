# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'name')

class EventSerializer(serializers.HyperlinkedModelSerializer):
	category = CategorySerializer()
	class Meta:
		model = Event
		fields = ('url', 'name', 'category', 'description', 'address', 'location', 'coordinate', 'date', 'start_time', 'end_time', 'image', 'active')