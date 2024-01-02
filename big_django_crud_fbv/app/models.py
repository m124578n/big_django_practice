from django.db import models

# Create your models here.

class Status(models.TextChoices):
    UNSTARTED = 'u'
    ONGOING = 'o'
    FINISHED = 'f'

class Task(models.Model):
    name = models.CharField(verbose_name="Task Name", max_length=65, unique=True)
    status = models.CharField(verbose_name="Task Status", max_length=1, choices=Status.choices)
    
    def __str__(self) -> str:
        return self.name
