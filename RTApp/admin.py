from django.contrib import admin
from RTApp.models import (
                            Detail, 
                            Standard, 
                            Section, 
                            Subject, 
                            Topic, 
                            Configuration,
                            Data,
                            )
# Register your models here.

admin.site.site_header = 'Robot-Teacher'
admin.site.index_title = 'Robot-Teacher'


class StandardAdmin(admin.ModelAdmin):
    list_display = ['std_id', 'std_name', 'std_created_at']
    list_per_page = 20

admin.site.register(Standard, StandardAdmin)

class SectionAdmin(admin.ModelAdmin):
    list_display = ['sec_id', 'standard', 'sec_name', 'sec_created_at']
    list_per_page = 20
admin.site.register(Section, SectionAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['sub_id', 'standard', 'sub_name', 'sub_created_at']
    list_per_page = 20
admin.site.register(Subject, SubjectAdmin)


class TopicAdmin(admin.ModelAdmin):
    list_display = ['topic_id', 'subject', 'topic_name', 'topic_created_at']
    list_per_page = 20
admin.site.register(Topic, TopicAdmin)


class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ['config_id', 'total_time', 'teaching_time', 'questions_time']
    list_per_page = 20
admin.site.register(Configuration, ConfigurationAdmin)

class DetailAdmin(admin.ModelAdmin):
    list_display = ['detail_id','teacher',]
    list_per_page = 20
admin.site.register(Detail, DetailAdmin)

class DataAdmin(admin.ModelAdmin):
    list_display = ['data_id', 'created_at', 'teacher', 'standard']
    list_per_page = 20
admin.site.register(Data, DataAdmin)


