from django.db import models


class ToDoCategoryModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250, default='')
    created = models.DateTimeField(auto_now_add=True)
    death_of_line = models.DateField(default=None, blank=True, null=True)

    @property
    def is_end(self):
        return self.all_todos_count == self.all_ended_todos_count

    @property
    def all_todos(self):
        return ToDoModel.objects.filter(category=self).all()

    @property
    def all_todos_count(self):
        return ToDoModel.objects.filter(category=self).count()

    @property
    def all_ended_todos(self):
        return ToDoModel.objects.filter(category=self, is_to_do=True).all()

    @property
    def all_ended_todos_count(self):
        return ToDoModel.objects.filter(category=self, is_to_do=True).count()


class ToDoModel(models.Model):
    task = models.CharField(max_length=50)
    detail = models.TextField(max_length=500, default=None, blank=True, null=True)
    is_to_do = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)
    death_of_line = models.DateField(default=None, blank=True, null=True)
    category = models.ForeignKey('ToDoCategoryModel', related_name='todo_category', on_delete=models.CASCADE)

