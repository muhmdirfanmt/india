"""indianhotel URL Configuration

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
from django.urls import path,include
from api.views import MenuItems,SpecificItem
from rest_framework_simplejwt.views import TokenVerifyView

from hotel.views import DishViewViewset,DishModelViewViewSetView
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("dishes",DishViewViewset,basename="dishes")
router.register("mdishes",DishModelViewViewSetView,basename="mdishes")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hotel/menu/',MenuItems.as_view()),
    path('hotel/menu/<int:mid>',SpecificItem.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('h/',include('hotel.url'))
]+router.urls
