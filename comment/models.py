from django.db import models
from django.contrib.auth.models import User
from blog.models import Post


class Comment(models.Model):
    article = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_date',)
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.body[:20]