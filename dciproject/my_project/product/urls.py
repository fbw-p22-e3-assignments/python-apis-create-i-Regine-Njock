from django.urls import path
from .views import ProductListCreateView, ProductRetrieveUpdateDestroyView

app_name = 'product'

urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product-list-create'),
    path('<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy'),
]