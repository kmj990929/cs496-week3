# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Answer)
admin.site.register(Song)
admin.site.register(Artist)
