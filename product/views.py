from rest_framework import generics
from rest_framework import permissions
from .models import Category, Product
from .serializers import ProductSerializer,CateforySerializer,RetriveProductSerializer,RetriveCategorySerializer

class ListProduct(generics.ListAPIView):
    permissions_class=[permissions.AllowAny,]

    serializer_class=ProductSerializer
    
    def get_queryset(self):
        return Product.objects.order_by('-id')
    
    
    
    


class ListCategory(generics.ListAPIView):
    permissions_class=[permissions.AllowAny,]
    queryset=Category.objects.all()
    serializer_class=CateforySerializer
    


class RetriveProduct(generics.RetrieveAPIView):
    permission_classes=[permissions.AllowAny,]
    queryset=Product.objects.all()
    serializer_class=RetriveProductSerializer
    lookup_field="slug"
    
    
class RetriveCategory(generics.RetrieveAPIView):
    permission_classes=[permissions.AllowAny,]
    queryset=Category.objects.all()
    serializer_class=RetriveCategorySerializer
    lookup_field="slug"
    
    
    
class CreateProduct(generics.CreateAPIView):
    permission_classes=[permissions.IsAdminUser,]
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    
class UpdateProduct(generics.UpdateAPIView):
    permission_classes=[permissions.IsAdminUser,]
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
class DeleteProduct(generics.DestroyAPIView):
    permission_classes=[permissions.IsAdminUser,]
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    
    
class CreateCategory(generics.CreateAPIView):
    permission_classes=[permissions.IsAdminUser,]
    queryset=Category.objects.all()
    serializer_class=CateforySerializer
    
class UpdateCategory(generics.UpdateAPIView):
    permission_classes=[permissions.IsAdminUser,]
    queryset=Category.objects.all()
    serializer_class=CateforySerializer
    
    
class DeleteCategory(generics.DestroyAPIView):
    permission_classes=[permissions.IsAdminUser,]
    queryset=Category.objects.all()
    serializer_class=CateforySerializer