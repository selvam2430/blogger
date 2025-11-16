from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

class Comments(models.Model):
    blog= models.ForeignKey(Blog, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    user = models.CharField(max_length=100, null=True, blank=True)

    