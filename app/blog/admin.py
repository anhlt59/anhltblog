from django.contrib import admin
from blog.models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # scope table only show attrs in list_display
    list_display = ("title", "slug", "author", "status")
    # edit filter sidebar
    list_filter = ("status", "created", "updated")
    # to search
    search_fields = ("author__username", "title")
    # auto generate field
    prepopulated_fields = {"slug": ("title",)}
    # scrope can edit in list_display
    list_editable = ("status",)
    # show date in list_display
    date_hierarchy = ("created")

# admin.site.register(Post, PostAdmin)
