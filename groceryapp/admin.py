from django.contrib import admin
from groceryapp.models import User,Category,Item,Order,Orderdone


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Orderdone)
