from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Tasks(models.Model):
    title = models.CharField(max_length=100, null= True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

# Create your models here.
