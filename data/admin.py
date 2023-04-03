from django.contrib import admin
from .models import StudentData
# Register your models here.


@admin.register(StudentData)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id","name","age","roll"]
