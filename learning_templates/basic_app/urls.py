from django.urls import path, include
from basic_app import views

app_name = 'basic_app'  # TEMPLATE TAGGING

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
