# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Picto,userlike,Profile


admin.site.register(Picto)
admin.site.register(userlike)
admin.site.register(Profile)
# Register your models here.
