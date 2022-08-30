from django.urls import path
from api import views

urlpatterns = [
    path('', views.QuarterViewSet.as_view(), name='quarter')
]