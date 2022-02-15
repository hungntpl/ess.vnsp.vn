"""ess URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    #Khi nào cần bật chế độ bảo trì thì enable lệnh bên dưới
    #path('', views.direct2python, name='direct2python'),
    path('', admin.site.urls),
    #path('admin/', admin.site.urls), 
    path('accounts/profile/', views.direct2epfile, name='direct2epfile'), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('vnspgallery/', include('gallery.urls')), 
    
    path('', include('wage.urls'), name = 'wage-print-notice'), 
    path('khaibaoyte/', RedirectView.as_view(url='https://tokhaiyte.vn/?page=Group.checkin&groupId=6092414e92bd219ab40fb32f')),
    path('dragontraining/', TemplateView.as_view(template_name="news/dragontraining.html")),
]



admin.site.site_header = "VNSP Employee Self Service Portal"
admin.site.site_title = "VNSP Employee Self Service Admin Portal"
admin.site.index_title = "Welcome to VNSP ESS Portal"