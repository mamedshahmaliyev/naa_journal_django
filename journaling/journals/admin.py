from django.contrib import admin

from .models import *

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

    list_filter = ('kafedra', 'student_group')

    def get_search_fields(self, request):
        return ['kafedra', 'student_group__name']
    
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

    list_filter = ('code',)

    def get_search_fields(self, request):
        return ['name', 'code']

@admin.register(JournalRecord)
class JournalRecordAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

    list_filter = ('journal__kafedra',)

    def get_search_fields(self, request):
        return ['journal__kafedra', 'student_group__name', 'subject__name', 'subject__code', 'student__name', 'student__surname']
