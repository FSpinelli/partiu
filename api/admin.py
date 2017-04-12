# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from api.models import *

admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Favorite)