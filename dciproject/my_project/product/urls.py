from django.urls import path
from .views import ProductListAPIView, ProductDetailAPIView

app_name = 'product'

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='product-list-create'),
    path('<str:product_name>/', ProductDetailAPIView.as_view(), name='product_detail'),
]
# class ProductCreate(generics.CreateAPIView):
#     # API endpoint that allows creation of a new customer
#     queryset = Product.objects.all(),
#     serializer_class = ProductSerializer


# class ProductList(generics.ListAPIView):
#     # API endpoint that allows customer to be viewed.
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductDetail(generics.RetrieveAPIView):
#     # API endpoint that returns a single customer by pk.
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductUpdate(generics.RetrieveUpdateAPIView):
#     # API endpoint that allows a customer record to be updated.
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductDelete(generics.RetrieveDestroyAPIView):
#     # API endpoint that allows a customer record to be deleted.
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer