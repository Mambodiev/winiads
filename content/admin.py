from django.contrib import admin
from . import models
from .models import Course, Video, Pricing, Subscription, OtherShopifyLinks,OtherAliexpressSuppliersLinks, Category, Store, Country, Gender, Age, Like, Order, AliexpressOrderGrowth, City, OrderItem




# @admin.register(models.Technology)
# class TechnologyAdmin(admin.ModelAdmin):
#     list_display = ('name', 'created_at', 'updated_at')
    


# @admin.register(models.OtherShopifyLinks)
class OtherShopifyLinksInline(admin.TabularInline):
    model = OtherShopifyLinks
    list_display = ('name', 'countries', 'created_at', 'updated_at')
    extra = 1
    classes = ('collapse', )

    
    
# @admin.register(models.OtherAliexpressSuppliersLinks)
class OtherAliexpressSuppliersLinksInline(admin.TabularInline):
    model = OtherAliexpressSuppliersLinks
    list_display = ('name', 'country', 'price', 'created_at', 'updated_at')
    extra = 1
    classes = ('collapse', )
    
    
# @admin.register(models.Store)
class StoreInline(admin.TabularInline):
    model = Store
    list_display = ('name', 'created_at', 'updated_at') 
    extra = 1
    classes = ('collapse', )

@admin.register(models.Category)
class Category(admin.ModelAdmin):
    model = Category
    list_display = ('name', 'created_at', 'updated_at')
   
@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at') 
    

@admin.register(models.Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at') 
    

@admin.register(models.Age)
class AgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at') 


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at') 
    

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
   list_display = ['ordered_date', 'ordered', ] 

# @admin.register(models.AliexpressOrderGrowth)
class AliexpressOrderGrowthInline(admin.TabularInline):
    model = AliexpressOrderGrowth
    list_display = ['name', 'order_quantity'] 
    extra = 1
    classes = ('collapse', )

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name_of_product', 'created_at', 'updated_at','button', 'countries','img_preview')
    readonly_fields = ['img_preview']

    inlines = [
        StoreInline, AliexpressOrderGrowthInline, OtherAliexpressSuppliersLinksInline, OtherShopifyLinksInline,  
    ]
    
    def get_prepopulated_fields(self, request, obj=None):
        return {
        'slug': ('name_of_product',),
        }
        
        
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'population')
    
    
admin.site.register(Course, CourseAdmin)
admin.site.register(Video)
admin.site.register(Pricing)
admin.site.register(Subscription)
admin.site.register(City, CityAdmin)
admin.site.register(OrderItem)
