from rest_framework import serializers
from .models import Category, Product
from django.utils.text import slugify
class CateforySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        
    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['category'] = {
            "id": instance.category.id,
            "title": instance.category.title,
            "slug": instance.category.slug
        }
        
        return context
    
    def update(self, instance, validated_data):
       contex=super().update(instance,validated_data)
       contex.slug=slugify(instance.title)
       contex.save()
       return contex 
       


class RetriveProductSerializer(serializers.ModelSerializer):
    related_product=serializers.SerializerMethodField(method_name='get_related_products')
    class Meta:
        model = Product
        fields =("id","category","title","slug","featured","price","description","thumbnail","related_product")
        
    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['category'] = {
            "id": instance.category.id,
            "title": instance.category.title,
            "slug": instance.category.slug
        }
        
        return context
    
    def get_related_products(self,obj):
        return ProductSerializer(obj.related,many=True).data



class RetriveCategorySerializer(serializers.ModelSerializer):
    products=serializers.SerializerMethodField(method_name='get_products')
    class Meta:
        model=Category
        fields=("id","title","products","slug","featured")
        
    def get_products(self,obj):
        return ProductSerializer(obj.products.all(),many=True).data
    
    
