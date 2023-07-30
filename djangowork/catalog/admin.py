from django.contrib import admin
from .models import Category, Good, ItemsDecor, Tag


class GoodAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "active", "category", "create", "update"]
    list_display_links = ["id", "name"]
    search_fields = ["name"]
    list_filter = ["price", "active"]


class GoodsAdminInLine(admin.StackedInline):
    model = Good.tags.through
    extra = 1


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'uuid']
    inlines = [GoodsAdminInLine]


admin.site.register(Category)
admin.site.register(Good, GoodAdmin)
admin.site.register(ItemsDecor)
admin.site.register(Tag, TagAdmin)


