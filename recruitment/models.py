from django.db import models


class Question(models.Model):
    content = models.TextField(verbose_name="内容")
    create_date = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    level = models.PositiveIntegerField(verbose_name='等级', default=1)
    is_public = models.BooleanField('是否公开', default=True)

    def __str__(self):
        return self.content[:20] + "..."


class AnswerForQuestion(models.Model):
    file = models.FileField(verbose_name="文件", upload_to='answer')
    create_date = models.DateTimeField('创建日期', auto_now_add=True)
    name = models.CharField(verbose_name="姓名", max_length=200)
    identity = models.CharField(verbose_name="学号", max_length=200)
    qq = models.CharField(verbose_name="qq号", max_length=200, null=True)
    wechat = models.CharField(verbose_name="微信号", max_length=200, null=True)
    email = models.EmailField(verbose_name="邮箱", null=True)

    def __str__(self):
        return self.name

