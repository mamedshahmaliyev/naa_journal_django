from django.contrib import admin

from .models import *

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

    # list_filter = ('name', 'surname')

    def get_search_fields(self, request):
        return ['name', 'surname']


@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    filter_horizontal = ('students',)

    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

    # list_filter = ('name', 'surname')

    def get_search_fields(self, request):
        return ['name', 'starosta__name', 'starosta__surname', 'students__name', 'students__surname']
