from django.db import models

# Create your models here.

class Post(models.Model):
    """A blogpost written by admin"""
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        """Return a string representation of the model"""
        return self.title