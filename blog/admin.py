from django.contrib import admin
from .models import Post, Comment, Category

admin.site.register(Comment)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'created_at', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
