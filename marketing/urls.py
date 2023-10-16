from django.urls import path
from . import views

urlpatterns = [
    path('customer_list/', views.customer_list_view, name='customer_list'),
    path('customer/<int:customer_id>/', views.customer_detail_view, name='customer_detail'),
    path('campaign/<int:campaign_id>/', views.campaign_detail_view, name='campaign_detail'),
    # add your other url patterns here
]
