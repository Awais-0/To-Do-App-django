from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'iscompleted', 'updated_at')
    search_fields = ('task',)


# Register your models here.
admin.site.register(Task, TaskAdmin)