from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.


class Standard(models.Model):
    std_id = models.AutoField(primary_key = True)
    std_name = models.CharField(max_length = 30, unique = True)
    std_description = models.TextField()
    std_created_at = models.DateTimeField(auto_now_add = True)    

    class Meta:
        verbose_name = 'Standard'
        verbose_name_plural = 'Standards'
        ordering = ('std_id',)   

    def __str__(self):
        return '{}'.format(self.std_name)

    def get_url(self):
        return reverse('RTApp:single-std', args = [self.std_id])


class Section(models.Model):
    sec_id = models.AutoField(primary_key = True)
    standard = models.ForeignKey(Standard, on_delete = models.CASCADE)
    sec_name = models.CharField(max_length =15)
    sec_description = models.TextField()
    sec_created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'
        ordering = ('-standard',)  

    def __str__(self):
        return '{}'.format(self.sec_name)
    def get_url(self):
        return reverse('RTApp:single-sec', args = [self.sec_id])


class Subject(models.Model):
    sub_id = models.AutoField(primary_key = True)
    standard = models.ForeignKey(Standard, on_delete = models.CASCADE)
    sub_name = models.CharField(max_length =40)
    sub_description = models.TextField()
    sub_created_at = models.DateTimeField(auto_now_add = True)
    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'
        ordering = ('sub_name',)
    def __str__(self):
        return '{}'.format(self.sub_name)
    def get_url(self):
        return reverse('RTApp:single-sub', args = [self.sub_id])

class Topic(models.Model):
    topic_id = models.AutoField(primary_key = True)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    topic_name = models.CharField(max_length = 100, null = False, blank = False)
    topic_description = models.TextField()
    topic_created_at = models.DateTimeField(auto_now_add = True)
    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'
        ordering = ('topic_name',)
    def __str__(self):
        return '{}'.format(self.topic_name) 
    def get_url(self):
        return reverse('RTApp:single-top', args=[self.topic_id])

class Configuration(models.Model):
    config_id = models.AutoField(primary_key = True)
    total_time = models.IntegerField(help_text = '***Enter time in mins') 
    teaching_time = models.IntegerField(help_text = '***Enter time in mins')
    questions_time = models.IntegerField(help_text = '***Enter time in mins')
    class Meta:
        verbose_name = "Configuration"
        verbose_name_plural = 'Configurations'
        ordering = ('-config_id', )
    def __str__(self):
        return '{}'.format(str(self.config_id))
    def get_url(self):
        pass

class Detail(models.Model):
    teacher = models.ForeignKey(User, on_delete= models.CASCADE)
    detail_id = models.AutoField(primary_key = True)
    created_at = models.DateTimeField(auto_now_add = True)
    standard = models.CharField(max_length = 25)
    section = models.CharField(max_length = 25)
    subject = models.CharField(max_length = 45)
    topic = models.CharField(max_length = 100)
    total_time = models.IntegerField(null=True)
    teaching = models.IntegerField(null=True)    
    questioning = models.IntegerField(null=True)
    class Meta:
        verbose_name = "Detail"
        verbose_name_plural = "Details"
        ordering = ('-created_at', )
    def __str__(self):
        return '{}'.format(str(self.created_at))
    def get_url(self):
        pass


class Data(models.Model):
    data_id = models.AutoField(primary_key = True)
    teacher = models.ForeignKey(User, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    standard = models.CharField(max_length = 25)
    section = models.CharField(max_length = 25)
    subject = models.CharField(max_length = 45)
    topic = models.CharField(max_length = 100)
    total_time = models.IntegerField(null=True)
    teaching = models.IntegerField(null=True)    
    questioning = models.IntegerField(null=True)
    class Meta:
        verbose_name = "Data"
        verbose_name_plural = "API-Data"
        ordering = ('-created_at', )
    def __str__(self):
        return '{}'.format(str(self.created_at))
    def get_url(self):
        pass
