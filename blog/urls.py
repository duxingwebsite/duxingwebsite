from django.conf.urls import url
from . import views

"""定义url模式"""
app_name = 'index'

urlpatterns = [
    # 主页
    url(r'^$', views.IndexView.as_view(), name='index'),
    # 文章页
    url(r'^post/(?P<slug>[^\\.]+)/$', views.PostView.as_view(), name='post'),
    # 分类页
    url(r'^category/(?P<slug>[^\\.]+)/$', views.CategoryView.as_view(), name='category'),
    # 标签页面
    url(r'^tag/(?P<slug>[^\\.]+)/$', views.TagView.as_view(), name='tag'),
]
