from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blog_list),
    path('blogs/<int:pk>/', views.blog_detail),
    path('country/<str:country_name>/', views.get_country_info),
]
