"""trydjango18 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from blog import views as blog_views
from blog import feed
from newsletter import views as news_views
from trydjango18 import views as try_views

urlpatterns = [

    url(r'^$', blog_views.BlogIndex, name='home'),
    url(r'^add/$',blog_views.BlogCreate, name='blog_create'),
    url(r'^(?P<id>\d+)$', blog_views.BlogDetail, name="entry_detail"),
    url(r'^(?P<id>\d+)/edit/$',blog_views.BlogUpdate, name='blog_edit'),
    url(r'^feed/$', feed.LatestPosts(), name='feed'),
    url(r'^newsletter/$', news_views.home, name='newsletter'),
    url(r'^contact/$', news_views.contact, name='contact'),
    url(r'^about/$', try_views.about, name='about'),
    url(r'^markdown/', include("django_markdown.urls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include("registration.backends.default.urls")),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)