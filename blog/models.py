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

    def comments(self):
        return self.comment_set.all()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    name = models.CharField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return f"{self.text[:50]}..."

class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    text = models.TextField()
    name = models.CharField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'reply'
        verbose_name_plural = 'replies'

    def __str__(self):
        return f"{self.text[:50]}..."