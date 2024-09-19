from django.contrib import admin
from .models import  Newbakes #,Popular,ItemSort

class NewbakesAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'current_price', 'size','category','flavour',  'layers_display', 'cakecategoryIdentifier',]  

# class PopularAdmin(admin.ModelAdmin):
#     list_display = ['name', 'image', 'current_price', 'size', 'category','flavour',  'layers_display',] 

# class ItemSortAdmin(admin.ModelAdmin):
#     list_display = ['name', 'image', 'current_price', 'size', 'category','flavour',  'layers_display',] 

admin.site.register(Newbakes, NewbakesAdmin),
# admin.site.register(Popular, PopularAdmin),
# admin.site.register(ItemSort, ItemSortAdmin)