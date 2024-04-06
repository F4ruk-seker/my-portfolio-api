from django.db import models


class ContactModel(models.Model):
    mail = models.EmailField(default=None, null=True, blank=True)
    website = models.URLField(default=None, null=True, blank=True)
    linkedin = models.URLField(default=None, null=True, blank=True)
    github = models.URLField(default=None, null=True, blank=True)


class ResumeModel(models.Model):
    name = models.CharField(max_length=100, default='')
    job_title = models.CharField(max_length=100, default='')
    picture = models.URLField(default=None, null=True, blank=True)
    contact = models.OneToOneField(ContactModel, on_delete=models.CASCADE, default=None, blank=True, null=True)
    description = models.TextField(default='')

