from django.contrib import admin
from . models import BlogPostImages, BlogCategory, BlogPost, FamousQuotes


admin.site.register(BlogCategory)
admin.site.register(BlogPostImages)
admin.site.register(BlogPost)
admin.site.register(FamousQuotes)