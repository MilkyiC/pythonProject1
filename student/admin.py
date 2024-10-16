from django.contrib import admin
from student import models
# Register your models here.

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('full_name','date_of_birth')

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('title','author','start_date','end_date')

@admin.register(models.Passport)
class PassportAdmin(admin.ModelAdmin):
    list_display=('full_name','series_number')

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=('title','hours')

@admin.register(models.Curator)
class CuratorAdmin(admin.ModelAdmin):
    list_display=('full_name','department')

@admin.register(models.Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display=('student','course','enrollment_date')