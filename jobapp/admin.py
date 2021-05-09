from django.contrib import admin
from jobapp.models import JobInfo, UserInfo
# Register your models here.


@admin.register(JobInfo)
class AdminJobInfo(admin.ModelAdmin):
    list_display = ['title', 'city', 'salary_tk']


@admin.register(UserInfo)
class MyUserInfo(admin.ModelAdmin):
    list_display = ['name', 'email']
