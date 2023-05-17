from django.contrib import admin

from .models import *


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

    # list_filter = ('name', 'surname')

    def get_search_fields(self, request):
        return ['name', 'surname']