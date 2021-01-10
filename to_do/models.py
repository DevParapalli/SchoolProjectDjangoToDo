from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

class ToDo(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    data = models.CharField(max_length=255, verbose_name="Reminders")
    updated_date_time = models.DateTimeField(verbose_name="Updated On", auto_now=True)
    dead_line = models.DateTimeField(verbose_name="Deadline",validators=[MinValueValidator(limit_value=timezone.now)])

    def __str__(self):
        return self.title