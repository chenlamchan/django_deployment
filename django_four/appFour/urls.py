from django.urls import path
from appFour import views

# Template Tagging
app_name = 'appFour'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
