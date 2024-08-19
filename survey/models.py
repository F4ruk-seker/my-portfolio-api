from django.db import models
# from cloudinary.models import CloudinaryField

import uuid


class SurveyUser(models.Model):  # is not a user
    username = models.TextField(default='')
    token = models.UUIDField(default=uuid.uuid4())
    token_expr = models.DateTimeField(null=True, blank=True)


class Survey(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pools = models.ManyToManyField('QuestionPool', related_name='surveys')


class QuestionPool(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()


class Question(models.Model):
    pool = models.ForeignKey(QuestionPool, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    question_type = models.CharField(max_length=50, choices=(('text', 'Text'), ('multiple_choice', 'Multiple Choice')))
    condition_question = models.ForeignKey('self', null=True, blank=True, related_name='conditioned_questions', on_delete=models.SET_NULL)
    condition_answer = models.CharField(max_length=200, null=True, blank=True)


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)


class Response(models.Model):
    question = models.ForeignKey(Question, related_name='responses', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, blank=True, null=True, default=True, on_delete=models.CASCADE)
    text = models.CharField(max_length=200, blank=True, null=True)


class Platform(models.Model):
    name = models.CharField(max_length=75)
    url = models.URLField(default=None, blank=True, null=True)
    color = models.CharField(max_length=20, help_text='hex, rgb, rgba')
    icon = models.ImageField(upload_to='platform')
