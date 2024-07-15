from django.db import models
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
    text = models.CharField(max_length=200)
