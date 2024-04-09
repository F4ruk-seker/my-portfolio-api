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
    # work_experiences = models.ManyToManyField('WorkExperiencesModel', blank=True, default=None)


class WorkExperiencesModel(models.Model):
    title = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    start_date = models.CharField(max_length=10)
    end_date = models.CharField(max_length=10)
    experience = models.TextField()
    show = models.BooleanField(default=True)

    # order = models.PositiveIntegerField(default=1)
    #
    # class Meta:
    #     ordering: tuple = 'order',

