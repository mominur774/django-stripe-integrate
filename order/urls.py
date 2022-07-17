from django.urls import path
from order import views

urlpatterns = [
    path('pricing-list/', views.pricing_list, name="pricing-list"),
    path('pricing-details/<int:id>/',
         views.pricing_details, name="pricing-details"),
]
