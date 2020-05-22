from django.shortcuts import render
from . serializers import GallerySerializer, GalleryCategorySerializer, ContactMessageSerializer
from . models import Gallery, Category, ContactMessage
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status


class CreateGalleryPost(CreateAPIView):
    serializer_class = GallerySerializer
    permission_classes = []
    queryset = Gallery.objects.all()


class ListGalleryPost(ListAPIView):
    serializer_class = GallerySerializer
    permission_classes = []
    queryset = Gallery.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            allCategories = Category.objects.all()
            serializedCategories = GalleryCategorySerializer(allCategories, many=True).data
            allGallery = Gallery.objects.all()
            serializedGalleryData = GallerySerializer(allGallery, many=True).data
            return Response({'success': True, 'gallery_data': serializedGalleryData,
                             'all_categories': serializedCategories}, status=status.HTTP_200_OK)

        except Exception as Err:
            print('Some error occurred')
            return Response({'success': False, 'message': 'Failed to fetch data'}, status=status.HTTP_400_BAD_REQUEST)


class ContactMessageCreate(CreateAPIView):
    serializer_class = ContactMessageSerializer
    permission_classes = []
    queryset = ContactMessage.objects.all()


class ContactMessageList(ListAPIView):
    serializer_class = ContactMessageSerializer
    permission_classes = []
    queryset = ContactMessage.objects.all()