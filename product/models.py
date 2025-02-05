from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)
    featured=models.BooleanField(default=False)
    class Meta:
        ordering=['title']
    
    def __str__(self) ->str:
        return self.title
    
    
class Product(models.Model):
    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)
    featured=models.BooleanField(default=False)
    thumbnail=models.URLField(null=True, blank=True)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    description=models.TextField(null=True)
    update_date=models.DateField(auto_now=True)
    
    def __str__(self) ->str:
        return self.title
    
    @property
    def related(self):
        return self.category.products.all().exclude(id=self.id)