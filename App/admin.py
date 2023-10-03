from django.contrib import admin

from App.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','name','email','semester','address','phone','batch')
admin.site.register(Student,StudentAdmin)