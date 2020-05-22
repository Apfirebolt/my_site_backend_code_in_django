from django.db import models
from . constants import GALLERY_CHOICES


class Category(models.Model):
    category_name = models.CharField(choices=GALLERY_CHOICES, max_length=150)
    category_image = models.ImageField(upload_to='category_images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.category_name)

    class Meta:
        verbose_name_plural = 'Category'


class Gallery(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    gallery_image = models.ImageField(upload_to='gallery')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.category) + ' - ' + str(self.title)

    class Meta:
        verbose_name_plural = 'Gallery'


class ContactMessage(models.Model):
    name = models.CharField("Name", max_length=200)
    email = models.EmailField("Email")
    message = models.TextField("Message")
    website = models.URLField("Website URL")

    def __str__(self):
        return str(self.name) + '-' + str(self.email)

    class Meta:
        verbose_name_plural = 'Contact Message'

