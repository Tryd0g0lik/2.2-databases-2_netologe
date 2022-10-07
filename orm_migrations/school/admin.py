from django.contrib import admin

from .models import Student, Teacher, School

class ScoolInline(admin.StackedInline):
    model = School
    extra = 0

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group']
    list_filter = ['teachers', 'group']
    inlines = [ScoolInline, ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    list_filter = ['subject']


