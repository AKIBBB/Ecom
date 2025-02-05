from django.urls import path
from .views import ListProduct,ListCategory,RetriveProduct,RetriveCategory,CreateProduct,UpdateProduct,DeleteProduct,CreateCategory,DeleteCategory,UpdateCategory

urlpatterns = [
    path('listproduct/', ListProduct.as_view(), name='listproduct'),
    path('listcategory/', ListCategory.as_view(), name='listcategory'),
    path('retrive_product/<str:slug>/',RetriveProduct.as_view(),name='retriveproduct'),
    path('retrive_category/<str:slug>/',RetriveCategory.as_view(), name='retrivecategory'),
    path('create_product/',CreateProduct.as_view(),name='create-product'),
    path('update_product/<int:pk>/',UpdateProduct.as_view(),name='update_product'),
    path('delete_product/<int:pk>/',DeleteProduct.as_view(),name='delete_product'),
    
    path('create_category/',CreateProduct.as_view(),name='create-category'),
    path('update_category/<int:pk>/',UpdateProduct.as_view(),name='update_category'),
    path('delete_category/<int:pk>/',DeleteProduct.as_view(),name='delete_category'),
    
]
