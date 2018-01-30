"""BlogSite URL Configuration

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
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^confirm-api/$', views.confirm),
    url(r'^get-tags-api/$', views.get_tags),
    url(r'^add-tag-api/$', views.add_tag),
    url(r'^delete-tag-api/$', views.delete_tag),
    url(r'^get-tag-article-api/$', views.get_tag_article),
    url(r'^add-article-api/$', views.add_article),
    url(r'^get-article-api/$', views.get_article),
    url(r'^index-get-article/$', views.index_get_article),
]
