from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """文章"""
    topic = models.CharField(verbose_name='标题', max_length=200)
    slug = models.CharField(verbose_name='英文标题', max_length=200)
    author = models.ForeignKey(User, verbose_name='作者', null=True, on_delete=models.SET_NULL, auto_created=True)
    summary = models.TextField(verbose_name='摘要')
    body = models.TextField(verbose_name='正文')
    category = models.ForeignKey('Category', verbose_name='分类', null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag', verbose_name='标签', blank=True)
    views = models.PositiveIntegerField('浏览量', default=0)
    create_date = models.DateTimeField('创建日期', auto_now_add=True)
    mod_time = models.DateTimeField('修改日期', auto_now=True)
    is_public = models.BooleanField('是否公开', default=True)

    def __str__(self):
        return self.topic

    class Meta:
        ordering = ['-create_date']
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return '/post/' + str(self.slug) + '/'


class Category(models.Model):
    """分类"""
    name = models.CharField(verbose_name='名称', max_length=20)
    slug = models.CharField(verbose_name='英文名称', max_length=20)
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    mod_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/categories/' + str(self.slug) + '/'

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    """标签"""
    name = models.CharField(verbose_name='标签名', max_length=20)
    slug = models.CharField(verbose_name='英文标签名', max_length=20)
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    mod_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/tags/' + str(self.slug) + '/'

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
