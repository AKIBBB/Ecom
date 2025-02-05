from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='user/images/')
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    
    


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class PurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchase_history')
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product_name}"

