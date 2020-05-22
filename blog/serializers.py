from rest_framework import serializers
from . models import BlogCategory, BlogPost, BlogPostImages, FamousQuotes, UncategorizedBlog, UnclassifiedBlogImages


class BlogCategorySerializer(serializers.ModelSerializer):
    number_of_blogs = serializers.SerializerMethodField()

    def get_number_of_blogs(self, obj):
        return obj.blog_category.count()

    class Meta:
        model = BlogCategory
        fields = ('category_name', 'category_slug', 'category_image', 'number_of_blogs',)
        extra_kwargs = {'category_slug': {'read_only': True}}


class BlogPostSerializer(serializers.ModelSerializer):
    all_sections = serializers.SerializerMethodField()

    def get_all_sections(self, obj):
        allSections = BlogPostImages.objects.filter(blog_related_to_id=obj.id)
        allSectionsData = BlogPostImageSerializer(allSections, many=True).data
        return allSectionsData

    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'blog_category', 'all_sections',)


class BlogPostImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPostImages
        fields = '__all__'


class FamousQuotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FamousQuotes
        fields = '__all__'


class UncategorizedBlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = UncategorizedBlog
        fields = '__all__'
        extra_kwargs = {'blog_slug': {'read_only': True}}


class UnclassifiedBlogImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = UnclassifiedBlogImages
        fields = '__all__'
