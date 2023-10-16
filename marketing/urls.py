from django.urls import path
from . import views

urlpatterns = [
    path('customer_list/', views.customer_list_view, name='customer_list'),
    path('customer/<int:customer_id>/', views.customer_detail_view, name='customer_detail'),
    path('customer/<int:customer_id>/edit/', views.edit_customer_view, name='edit_customer'),
    path('customer/<int:customer_id>/add_campaign/', views.add_campaign_view, name='add_campaign'),
    path('campaign/<int:campaign_id>/', views.campaign_detail_view, name='campaign_detail'),
    # add your other url patterns here
]
