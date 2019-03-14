from django.urls import path

from stasher.customers.views import CustomerListAPIView, CustomerDetailAPIView


urlpatterns = [
    path('', CustomerListAPIView.as_view()),
    path('<str:id_>/', CustomerDetailAPIView.as_view())
]
