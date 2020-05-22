from django.shortcuts import render
from . models import BlogCategory, BlogPost, BlogPostImages, FamousQuotes, UnclassifiedBlogImages, UncategorizedBlog
from . serializers import ( BlogCategorySerializer, BlogPostSerializer, BlogPostImageSerializer, FamousQuotesSerializer,
                          UncategorizedBlogSerializer, UnclassifiedBlogImages, UnclassifiedBlogImagesSerializer)
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status


class CreateBlogCategory(CreateAPIView):
    permission_classes = []
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer


class ListBlogCategory(ListAPIView):
    permission_classes = []
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer


class EditDeleteBlogCategory(RetrieveUpdateDestroyAPIView):
    permission_classes = []
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    lookup_field = 'category_slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        allPosts = BlogPost.objects.filter(blog_category_id=instance.id)
        allPostsData = BlogPostSerializer(allPosts, many=True).data
        data['all_posts'] = allPostsData
        return Response({'success': True, 'data': data}, status=status.HTTP_200_OK)


class CreateBlogPost(CreateAPIView):
    permission_classes = []
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()


class ListBlogPost(ListAPIView):
    permission_classes = []
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class CreateBlogPostImage(CreateAPIView):
    permission_classes = []
    queryset = BlogPostImages.objects.all()
    serializer_class = BlogPostImageSerializer


class ListBlogPostImage(ListAPIView):
    permission_classes = []
    queryset = BlogPostImages.objects.all()
    serializer_class = BlogPostImageSerializer


class ListFamousQuotes(ListAPIView):
    permission_classes = []
    queryset = FamousQuotes.objects.all()
    serializer_class = FamousQuotesSerializer


class CreateFamousQuotes(CreateAPIView):
    permission_classes = []
    queryset = FamousQuotes.objects.all()
    serializer_class = FamousQuotesSerializer


class CreateUnclassifiedBlog(CreateAPIView):
    permission_classes = []
    queryset = UncategorizedBlog.objects.all()
    serializer_class = UncategorizedBlogSerializer


class ListUnclassifiedBlog(ListAPIView):
    permission_classes = []
    queryset = UncategorizedBlog.objects.all()
    serializer_class = UncategorizedBlogSerializer


class CreateUnclassifiedBlogImages(CreateAPIView):
    permission_classes = []
    queryset = UnclassifiedBlogImages.objects.all()
    serializer_class = UnclassifiedBlogImagesSerializer


class ListUnclassifiedBlogImages(ListAPIView):
    permission_classes = []
    queryset = UnclassifiedBlogImages.objects.all()
    serializer_class = UnclassifiedBlogImagesSerializer


class RetrieveUnclassifiedBlogDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = []
    queryset = UncategorizedBlog.objects.all()
    serializer_class = UncategorizedBlogSerializer
    lookup_field = 'blog_slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        blogImages = UnclassifiedBlogImages.objects.filter(related_blog_id=instance.id)
        blogImagesData = UnclassifiedBlogImagesSerializer(blogImages, many=True).data
        data['blog_images'] = blogImagesData
        return Response({'success': True, 'data': data}, status=status.HTTP_200_OK)