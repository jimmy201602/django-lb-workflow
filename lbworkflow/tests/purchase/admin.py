from django.contrib import admin

from .models import Purchase

from .models import Item


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'reason')


admin.site.register(Purchase, PurchaseAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('purchase', 'name', 'qty', 'note')


admin.site.register(Item, ItemAdmin)
