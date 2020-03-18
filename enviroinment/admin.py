from django.contrib import admin

# Register your models here.
from core.admin import BaseModelAdmin
from enviroinment.models import Enviroinment, Project

admin.site.register(Enviroinment, BaseModelAdmin)
admin.site.register(Project, BaseModelAdmin)
