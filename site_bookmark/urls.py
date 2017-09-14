"""site_bookmark URL Configuration

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

from bookmark.models import Bookmark
from django.views.generic import ListView,DetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bookmark/$', ListView.as_view(model=Bookmark), name='index'),
    # 정규표현식에서 ^는 시작 $는 끝을 의미, ()는 그룹을 지정
    # pk는 primary key(를 의미 d는 digit, +는 숫자가 하나 이상
    url(r'^bookmark/(?P<pk>\d+)/$', DetailView.as_view(model=Bookmark),name='detail')
]
