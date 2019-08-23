from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import F
from .models import Post, Tag, Category


class IndexView(ListView):
    """主页"""
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.get_pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)
        return context

    def get_queryset(self):
        return super().get_queryset().filter(is_public=True)

    # 获取分页信息
    @staticmethod
    def get_pagination_data(paginator, page, is_paginated):
        if not is_paginated:
            return {}
        page_number = page.number
        max_page_number = paginator.num_pages
        left_has_more = bool(page_number - 2 > 1)
        right_has_more = bool(page_number + 2 < max_page_number)
        if left_has_more:
            left = list(range(page_number - 1, page_number))
        else:
            left = list(range(1, page_number))
        if right_has_more:
            right = list(range(page_number + 1, page_number + 2))
        else:
            right = list(range(page_number + 1, max_page_number + 1))
        return {
            'left': left,
            'right': right,
            'right_has_more': right_has_more,
            'left_has_more': left_has_more,
            'max_page_number': max_page_number,
        }


class CategoryView(IndexView):
    """分类页面"""
    template_name = 'blog/category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return super().get_queryset().filter(category=category)


class TagView(CategoryView):
    """标签页面"""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        tags = get_object_or_404(Tag, slug=self.kwargs.get('slug'))
        return super().get_queryset().filter(tags=tags)


class PostView(DetailView):
    """文章详细页面"""
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'

    def get_queryset(self):
        return super().get_queryset().filter(is_public=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        Post.objects.filter(pk=self.object.pk).update(views=F('views') + 1)
        return response