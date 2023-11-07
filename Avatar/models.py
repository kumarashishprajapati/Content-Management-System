from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    publication_date = models.DateField()
    tags = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='Files/', blank=True, null=True)
# You can extend the User model for custom user roles
    def __str__(self):
        return str(id)