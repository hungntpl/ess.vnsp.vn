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
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

def direct2python(request):
    
    #html = '<h1> <center> Hệ thống đang được bảo trì, xin vùi lòng quay lại sau, xin cảm ơn !!! <center> </h1>'


    #return HttpResponse(html)
    #return render_to_response("maintainads.html")
    return render(request, "maintainads/maintainads.html")


def direct2epfile(request):
    response = redirect('/eprofile/efile/')
    return response
