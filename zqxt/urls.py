"""zqxt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from testapp.views import *

urlpatterns = [
    # 普通用户的访问操作
    url(r'^$',web), #默认主页
    url(r'^web/',web,name='index'),#网站主页
    url(r'^room/',room,name='web'),#获取房间信息
    url(r'^food/',food,name='food'),#获取餐饮分页信息
    url(r'^mon/',mon,name='mon'), #获取交易分页数据
    url(r'^spe/',spe,name='spe'),#获取特产分页信息

    # 普通用户的登录、注册、退出
    url(r'^login/',login,name='login'), #用户登录
    url(r'^sign/',sign,name='sign'), #用户注册
    url(r'^about/',about,name='about'),#网站的关于信息
    url(r'^exit/',exit,name='exit'), #退出

    url(r'^post/',post,name='post'), #发布交易信息
    url(r'^info/',info,name='info'),#查看个人信息

    # 以下是管理员的操作
    # 获取管理数据
    url(r'^rhyadm/',rhyadm,name='rhyadm'),#管理登录界面
    url(r'^admroom/',admroom,name='admroom'),#获取房间分页数据
    url(r'^admfood/',admfood,name='admfood'),#获取食物分页数据
    url(r'^admspe/',admspe,name='admspe'),#获取特产分页数据
    url(r'^admmon/',admmon,name='admmon'),#获取交易分页数据
    url(r'^admuser/',admuser,name='admuser'),#获取用户分页数据

    # 添加房间、菜品
    url(r'^roomadd/',roomadd,name='roomadd'),#管理员添加房间信息
    url(r'^foodadd/',foodadd,name='foodadd'),#管理员添加菜品
    url(r'^speadd/',speadd,name='speadd'),#管理员添加特产

    # 修改房间、菜品信息
    url(r'^roommod/',roommod,name='roommod'),#管理员修改房间信息
    url(r'^foodmod/',foodmod,name='foodmod'),#管理员修改菜品信息

    # 信息删除操作
    url(r'^roomdel/',roomdel,name='roomdel'),#管理员删除房间
    url(r'^fooddel/',fooddel,name='fooddel'),#管理员删除菜品
    url(r'^spedel/',spedel,name='spedel'),#管理员删除特产
    url(r'^mondel/',mondel,name='mondel'),#管理员删除交易
    url(r'^userdel/',userdel,name='userdel'),#管理员删除用户

    #管理员退出、添加、修改
    url(r'^admexit/',admexit,name='admexit'),
    url(r'^admaddmod/',admaddmod,name='admaddmod'),
]
