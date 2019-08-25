from django.conf.urls import url
from . import views

"""定义url模式"""
app_name = 'recruitment'

urlpatterns = [
    # 主页
    url(r'^$', views.index, name="index"),
    # 问题页面
    url(r'^question$', views.QuestionView.as_view(), name='question'),
    # 提交答案页面
    url(r'^answer-submit$', views.CreateAnswerView.as_view(), name='answer-submit'),
    # 谢谢页面
    url(r'^thanks$', views.thanks, name='thanks'),
]
