from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

# Questions for Poll
class Question(models.Model):
  """ Model for poll questions """

  text = models.CharField(max_length = 200)
  date_published = models.DateTimeField()

  def __str__(self):
    return self.text

  def was_published_recently(self):
    return timezone.now() - self.date_published < datetime.timedelta(days=2)

# Choices for Poll
class Choice(models.Model):
  """ Model for poll choices for each question """

  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  text = models.CharField(max_length = 200)
  votes = models.IntegerField(default = 0)

  def __str__(self):
    return self.text