from django.contrib import admin

from .models import Log, Project


class LogsInLine(admin.TabularInline):
    model = Log
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name']
    search_fields = ['project_name']

    fieldsets = [
        (None, {'fields': ['project_name', 'user']}),
    ]
    inlines = [LogsInLine]

admin.site.register(Project, ProjectAdmin)
