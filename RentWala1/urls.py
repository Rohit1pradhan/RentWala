"""RentWala URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from api import views
from api.views import register, registeration

urlpatterns = [
    path("",views.home),
    path('admin/', admin.site.urls),
    path('register/',views.register),
    path('registration/',views.registeration.as_view()),
    path('login',views.login),
    # path('forgetpassword/',views.forgetpassword),
    path('forpassword/',views.forpassword),
    path('forgetpassword/',views.ForgetPassword.as_view()),
    path('resetpassword/',views.ResetPassword.as_view()),
    # path('activate/',views.activate),
    path('activate/',views.actavation.as_view()),
    path('search/',views.searchfortanent),
    path('alluser/',views.allusers),
    path('addproparty/',views.addproparty),
    path('addhome/',views.addhouse.as_view()),
    # path('demo/',views.demo.as_view()),
    # path('demo1/',views.demo1.as_view())

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

