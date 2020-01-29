from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from article import views                                
        
router = routers.DefaultRouter()                      # add this
router.register(r'article', views.ArticleView, 'article')     # add this
        
urlpatterns = [
    path('admin/', admin.site.urls),           
    path('api/', include(router.urls))                # add this
]