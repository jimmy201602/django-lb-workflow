from django.contrib import admin

from .models import Issue


class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'content')


admin.site.register(Issue, IssueAdmin)
