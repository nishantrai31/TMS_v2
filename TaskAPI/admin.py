from TaskAPI.models import Comment, Task, Project, TaskAssignment
from django.contrib import admin


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display= ['id','title','status', 'priority','due_date']

    list_filter = ("status","priority")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display= ['id','name','start_date', 'end_date']

    list_filter = ("name","start_date")

@admin.register(TaskAssignment)
class TaskAssignmentAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display= ['id','task','user']

    list_filter = ("task","user")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display= ['id','task','text']

    list_filter = ("task","user")