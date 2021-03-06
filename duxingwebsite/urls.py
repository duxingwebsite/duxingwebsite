"""duxingwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.static import serve
from django.views.generic.base import RedirectView
from . import settings

urlpatterns = [
    # 管理界面
    path('admin/', admin.site.urls),
    # 网站图标
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon/favicon.png')),
    # 主页
    path('', include('index.urls', namespace='index')),
    # 博客
    path('blog/', include('blog.urls', namespace='blog')),
    # 招新
    path('recruitment/', include('recruitment.urls', namespace='recruitment')),
    # 评论
    path('comment/', include('comment.urls', namespace='comment')),
    # 媒体文件
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
