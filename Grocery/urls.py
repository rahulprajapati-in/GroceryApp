"""Grocery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from groceryapp import views
from Grocery import settings

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('indexcategory/', views.indexcategory, name='indexcategory'),
    path('addcate/', views.addcate, name='addcate'),
    path('displaycategory/', views.displaycategory, name='displaycategory'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('index/', views.index, name='index'),
    path('item/', views.item, name='item'),
    path('cart/', views.cart, name='cart'),
    path('checkout/',views.checkout, name='checkout'),
    path('login/',views.login, name='login'),
    path('registeraction/',views.registeraction, name='registeraction'),
    path('loginaction/',views.loginaction, name='loginaction'),
    path('checkout1/',views.checkout1, name='checkout1'),
    path('indexaction/',views.indexaction, name='indexaction'),
    path('delateaction/',views.delateaction, name='delateaction'),
    # path('rahul/',views.rahul,name=rahul)
    path('logout/',views.logout,name='logout'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services')


] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
