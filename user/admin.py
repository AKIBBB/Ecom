from django.contrib import admin
from .import models
from .models import UserProfile, PurchaseHistory
from django.contrib.auth.models import User

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','image' ]
    
    def first_name(self,obj):
        return obj.user.first_name
    
    
    def last_name(self,obj):
        return obj.user.last_name
    
admin.site.register(models.Customer,CustomerAdmin)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "Profile"
    extra = 0

# Extend UserAdmin to include profile details
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active']
    search_fields = ['username', 'email']
    inlines = [UserProfileInline]

# Registering User with UserProfile Inline
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register PurchaseHistory
@admin.register(PurchaseHistory)
class PurchaseHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'product_name', 'price', 'purchase_date']
    search_fields = ['user__username', 'product_name']
    list_filter = ['purchase_date']