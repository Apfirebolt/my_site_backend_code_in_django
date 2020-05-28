from django.urls import path
from django.views.generic import TemplateView
from . views import (blog_test, CreateBlogCategory, ListBlogCategory, EditDeleteBlogCategory, CreateFamousQuotes, ListFamousQuotes,
                      CreateUnclassifiedBlog, ListUnclassifiedBlog, CreateUnclassifiedBlogImages,
                      ListUnclassifiedBlogImages, RetrieveUnclassifiedBlogDetail, CreateBlogPost, ListBlogPost,
                      ListBlogPostImage, CreateBlogPostImage, UpdateBlogPostImage, UpdateUnclassifiedBlogImages)


urlpatterns = [
    path('', TemplateView.as_view(template_name='blog/blog_home.html'), name='home'),
    path('test', blog_test, name='blog-test'),
    path('blog-category/create', CreateBlogCategory.as_view(), name='blog-category-create'),
    path('blog-category/list', ListBlogCategory.as_view(), name='blog-category-list'),
    path('blog-post/create', CreateBlogPost.as_view(), name='blog-post-create'),
    path('blog-post-image/list', ListBlogPostImage.as_view(), name='blog-post-image-list'),
    path('blog-post-image/create', CreateBlogPostImage.as_view(), name='blog-post-image-create'),
    path('blog-post-image/<int:pk>', UpdateBlogPostImage.as_view(), name='blog-post-image-update'),
    path('blog-post/list', ListBlogPost.as_view(), name='blog-post-list'),
    path('blog-category/<str:category_slug>', EditDeleteBlogCategory.as_view(), name='blog-category-update'),
    path('quotes/list', ListFamousQuotes.as_view(), name='quote-list'),
    path('quotes/create', CreateFamousQuotes.as_view(), name='quote-create'),
    path('unclassified/create', CreateUnclassifiedBlog.as_view(), name='unclassified-create'),
    path('unclassified/list', ListUnclassifiedBlog.as_view(), name='unclassified-list'),
    path('unclassified-image/create', CreateUnclassifiedBlogImages.as_view(), name='unclassified-image-create'),
    path('unclassified-image/list', ListUnclassifiedBlogImages.as_view(), name='unclassified-image-list'),
    path('unclassified-image/<int:pk>', UpdateUnclassifiedBlogImages.as_view(), name='unclassified-image-update'),
    path('unclassified/<str:blog_slug>', RetrieveUnclassifiedBlogDetail.as_view(), name='update-blog-detail')
]