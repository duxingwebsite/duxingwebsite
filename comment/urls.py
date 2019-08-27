from django.conf.urls import url
from . import views

"""定义url模式"""
app_name = 'comment'

urlpatterns = [
    # 发表评论
    url(r'^post-comment/(?P<article_id>\d+)/$', views.post_comment, name='post_comment'),
]

