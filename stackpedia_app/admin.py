from django.contrib import admin
from .models import Post, Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields: dict({'slug': ('title',),})

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields: dict({'slug': ('title',),})


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)