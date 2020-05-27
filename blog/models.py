from django.db import models
from django.utils.text import slugify


class BlogCategory(models.Model):
    category_name = models.CharField("Category Name", max_length=100)
    category_slug = models.SlugField(unique=True, blank=True, null=True)
    category_image = models.FileField(upload_to='blog_category_images', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.category_slug = slugify(self.category_name)
            super(BlogCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name

    class Meta:
        '''Doc string for meta'''
        verbose_name_plural = "Category Name"


class BlogPost(models.Model):
    title = models.CharField("Blog Title", max_length=200)
    content = models.TextField("Blog Content", blank=False)
    blog_category = models.ForeignKey(BlogCategory, related_name='blog_category', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.blog_category) + ' - ' + str(self.title)

    class Meta:
        '''Doc string for meta'''
        verbose_name_plural = "Blog Post"


class BlogPostImages(models.Model):
    blog_related_to = models.ForeignKey(BlogPost, related_name='related_blog_post', on_delete=models.CASCADE)
    blog_image = models.FileField("Blog Image", upload_to='blog_images')
    created_at = models.DateTimeField("Created At", null=True, blank=True, auto_now=True)
    image_description = models.TextField("Image Description", null=True, blank=True, default="No description available")

    def __str__(self):
        return str(self.blog_related_to)

    class Meta:
        '''Doc string for meta'''
        verbose_name_plural = "Blog Images"


class FamousQuotes(models.Model):
    content = models.CharField(max_length=300)
    quoted_by = models.CharField(max_length=100)

    def __str__(self):
        return str(self.quoted_by)

    class Meta:
        '''Doc string for meta'''
        verbose_name_plural = "Famous Quotes"


class UncategorizedBlog(models.Model):
    title = models.CharField("Uncategorized Blog Title", max_length=200)
    content = models.TextField("Uncategorized Blog Content", blank=False)
    blog_slug = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.blog_slug = slugify(self.title)
        super(UncategorizedBlog, self).save(*args, **kwargs)


    def __str__(self):
        return str(self.title)

    class Meta:
        '''Doc string for meta'''
        verbose_name_plural = "Uncategorized Blog Posts"


class UnclassifiedBlogImages(models.Model):
    related_blog = models.ForeignKey(UncategorizedBlog, on_delete=models.CASCADE)
    blog_image = models.ImageField(upload_to='unclassified_blog_images')
    image_description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.image_description)

    class Meta:
        '''Doc string for meta'''
        verbose_name_plural = "Uncategorized Blog Posts Images"


