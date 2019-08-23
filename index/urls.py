from django.conf.urls import url
from . import views

"""定义url模式"""
app_name = 'index'

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
]
