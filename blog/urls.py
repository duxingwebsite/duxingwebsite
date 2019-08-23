from django.conf.urls import url
from . import views

"""定义url模式"""
app_name = 'index'

urlpatterns = [
    # 主页
    url(r'^$', views.IndexView.as_view(), name='index'),
    # 文章页
    url(r'^post/(?P<slug>[^\\.]+)/$', views.PostView.as_view(), name='post'),
    # 标签页
    url(r'^category/(?P<slug>[^\\.]+)/$', views.CategoryView.as_view(), name='category'),
]
