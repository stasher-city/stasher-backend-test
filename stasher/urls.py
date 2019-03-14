from django.urls import path, include


urlpatterns = [
    path('customers/', include('stasher.customers.urls')),
]
