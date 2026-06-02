from django.contrib import admin
from .models import Category, Transaction

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'type')
    search_fields = ('user__username', 'user__email', 'name')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'category', 'amount', 'date')
    search_fields = ('user__username', 'user__email', 'amount')
    list_filter = ('date', 'category__type', 'category__name')
    list_select_related = ('user', 'category')