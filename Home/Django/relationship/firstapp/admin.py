from django.contrib import admin
from .models import *

admin.site.register([Interest, City, Person, Country])
