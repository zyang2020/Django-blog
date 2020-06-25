from django.contrib import admin
from blogging.models import Post, Category


# for many to many InlineModelAdmin
class MyInline(admin.TabularInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    inlines = [MyInline, ]

class CategoryAdmin(admin.ModelAdmin):
    inlines = [MyInline, ]
    exclude = ('posts',)

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
