from django.contrib import admin
from app.models import *
#class appadmin(admin.ModelAdmin):

admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Clothe)
admin.site.register(Commodity)
admin.site.register(SKU)
admin.site.register(Pic)
admin.site.register(ClotheSku)