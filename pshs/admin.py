from django.contrib import admin
from .models import Question, Attendance




class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


class AttendanceAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Attendance, AttendanceAdmin)
# Register your models here.
