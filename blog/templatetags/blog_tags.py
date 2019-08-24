from ..models import Post, Tag, Category
from django.db.models.aggregates import Count
from django import template
import markdown

register = template.Library()


@register.simple_tag
def get_recent_article_list(num=15):
    """获取最近文章"""
    return Post.objects.filter(is_public=True).order_by('-create_date')[:num]


@register.simple_tag
def get_article_count():
    """获取文章数量"""
    return Post.objects.filter(is_public=True).count()


@register.simple_tag
def get_next_article_name(article):
    """获取下一篇文章的名称"""
    next_article = Post.objects.filter(pk=(article.pk + 1)).filter(is_public=True)
    if next_article:
        return next_article[0].topic
    else:
        return None


@register.simple_tag
def get_preview_article_name(article):
    """获取上一篇文章的名称"""
    preview_article = Post.objects.filter(pk=(article.pk - 1)).filter(is_public=True)
    if preview_article:
        return preview_article[0].topic
    else:
        return None


@register.simple_tag
def get_archives_data():
    """获取归档信息"""
    date_list = Post.objects.filter(is_public=True).datetimes('create_date', 'month', 'DESC')
    date_dict = {}
    for date in date_list:
        if date_dict.get(date.year):
            date_dict[date.year].append(date.month)
        else:
            date_dict[date.year] = []
            date_dict[date.year].append(date.month)
    return sorted(date_dict.items(), reverse=True)


@register.simple_tag
def get_tags():
    """获取标签信息"""
    return Tag.objects.filter(article__is_public=True).annotate(article_num=Count('article')).order_by(
        '-article_num').filter(article_num__gt=0)


@register.simple_tag
def get_tag_count():
    """获取标签数量"""
    return Tag.objects.filter(article__is_public=True).count()


@register.simple_tag
def get_categories():
    """获取分类信息"""
    return Category.objects.filter(article__is_public=True).annotate(article_num=Count('article')).order_by(
        '-article_num').filter(article_num__gt=0)


@register.simple_tag
def get_category_count():
    """获取分类数量"""
    return Category.objects.filter(article__is_public=True).count()


@register.simple_tag
def markdown_text(text):
    """markdown渲染"""
    html = markdown.markdown(text,
                             extensions=[
                                 'markdown.extensions.extra',
                                 'markdown.extensions.codehilite',
                             ])
    return html


@register.simple_tag
def get_article_tags(article):
    """获取文章标签"""
    return article.tags.all()
