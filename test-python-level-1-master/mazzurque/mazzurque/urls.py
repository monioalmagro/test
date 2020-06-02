from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from ejercicio.views import FisicaViewSet , JuridicaViewSet



routers = DefaultRouter()
routers.register(r'fisica',FisicaViewSet, basename='fisica')
routers.register(r'juridica',JuridicaViewSet)
urlpatterns = routers.urls


urlpatterns += [
    path('admin/', admin.site.urls),
   
]
