from ..models import Post, Tag, Category
from comment.models import Comment
from django.db.models.aggregates import Count
from django import template
import markdown

register = template.Library()


@register.simple_tag
def get_recent_post_list(num=15):
    """获取最近文章"""
    return Post.objects.filter(is_public=True).order_by('-create_date')[:num]


@register.simple_tag
def get_post_count():
    """获取文章数量"""
    return Post.objects.filter(is_public=True).count()


@register.simple_tag
def get_next_post_name(post):
    """获取下一篇文章的名称"""
    next_post = Post.objects.filter(pk=(post.pk + 1)).filter(is_public=True)
    if next_post:
        return next_post[0].topic
    else:
        return None


@register.simple_tag
def get_preview_post_name(post):
    """获取上一篇文章的名称"""
    preview_post = Post.objects.filter(pk=(post.pk - 1)).filter(is_public=True)
    if preview_post:
        return preview_post[0].topic
    else:
        return None


@register.simple_tag
def get_tags():
    """获取标签信息"""
    return Tag.objects.filter(post__is_public=True).annotate(post_num=Count('post')).order_by(
        '-post_num').filter(post_num__gt=0)


@register.simple_tag
def get_tag_count():
    """获取标签数量"""
    return Tag.objects.filter(post__is_public=True).count()


@register.simple_tag
def get_categories():
    """获取分类信息"""
    return Category.objects.filter(post__is_public=True).annotate(post_num=Count('post')).order_by(
        '-post_num').filter(post_num__gt=0)


@register.simple_tag
def get_category_count():
    """获取分类数量"""
    return Category.objects.filter(post__is_public=True).count()


@register.simple_tag
def markdown_text(text):
    """markdown渲染"""
    config = {
        'codehilite': {
            'use_pygments': True,
        }
    }
    html = markdown.markdown(text,
                             extensions=[
                                 'markdown.extensions.extra',
                                 'markdown.extensions.codehilite',
                                 "markdown.extensions.toc",
                             ],
                             extensions_configs=config)
    return html


@register.simple_tag
def get_post_tags(post):
    """获取文章标签"""
    return post.tags.all()


@register.simple_tag
def get_article_count_in_a_category(category):
    """获取某个分类下的文章数量"""
    return Post.objects.filter(is_public=True, category=category).count()


@register.simple_tag
def get_post_comments(article_id):
    """获取某个文章下的评论"""
    return Comment.objects.filter(article=article_id)
