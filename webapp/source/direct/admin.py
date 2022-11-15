from django.contrib import admin
from .models import *

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', )


class SupervisorAdmin(admin.ModelAdmin):
    pass

class AdministratorAdmin(admin.ModelAdmin):
    pass

class StudentGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course')

class StudentAdmin(admin.ModelAdmin):
    pass

class DisciplineAdmin(admin.ModelAdmin):
    pass


admin.site.register(Administrator, AdministratorAdmin)
admin.site.register(Supervisor, SupervisorAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(StudentGroup, StudentGroupAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Discipline, DisciplineAdmin)
