from django.contrib import admin
<<<<<<< HEAD
from .models import Post, Comment, Category
=======
from .models import Post, Comment, Categories, Rate
>>>>>>> 1eb85dca06f7d85571f1f321a84ba3bfe0ba2c87

admin.site.register(Comment)
<<<<<<< HEAD

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
=======
admin.site.register(Categories)
admin.site.register(Rate)
>>>>>>> 1eb85dca06f7d85571f1f321a84ba3bfe0ba2c87
