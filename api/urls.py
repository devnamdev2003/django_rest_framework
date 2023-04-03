from django.contrib import admin
from django.urls import path
from data import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.index),
    path('api/insert', views.insert),
    path('api/<int:i>', views.fetch),
    path('api/remove/<int:i>', views.remove),
    path('', views.home),
    path('view/<int:pk>', views.view),
    path('view/', views.view),
]
