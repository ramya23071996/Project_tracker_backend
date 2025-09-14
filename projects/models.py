from django.db import models
from django.contrib.auth.models import User

class MiniProject(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='miniprojects')
    status = models.CharField(max_length=30, choices=[('inprogress', 'In Progress'), ('completed', 'Completed')], default='inprogress')
    priority = models.CharField(max_length=10, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    due_date = models.DateField()

    def __str__(self):
        return self.title
