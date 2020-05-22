from rest_framework import serializers
from . models import Gallery, Category, ContactMessage


class GallerySerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    def get_category_name(self, obj):
        return obj.category.category_name

    class Meta:
        model = Gallery
        fields = ('category', 'title', 'description', 'created_at', 'gallery_image', 'likes', 'category_name',)


class GalleryCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ContactMessageSerializer(serializers.ModelSerializer):
    website = serializers.URLField(required=False, allow_blank=True)

    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'website', 'message',)