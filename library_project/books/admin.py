from django.contrib import admin
from .models import Book, Category, Feedback

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'publication_date', 'created_at')
    list_filter = ('category', 'publication_date')
    search_fields = ('title', 'author', 'description')
    date_hierarchy = 'publication_date'

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('subject', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('subject', 'message', 'user__username')