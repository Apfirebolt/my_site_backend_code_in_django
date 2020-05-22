from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView
from . models import Project, ProjectImages
from . serializers import ProjectImageSerializer, ProjectSerializer
from rest_framework.response import Response
from rest_framework import status


class CreateProject(CreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = []


class ListProject(ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = []


class CreateProjectImage(CreateAPIView):
    serializer_class = ProjectImageSerializer
    queryset = ProjectImages.objects.all()
    permission_classes = []


class ListProjectImages(ListAPIView):
    serializer_class = ProjectImageSerializer
    queryset = ProjectImages.objects.all()
    permission_classes = []


class UpdateDestroyProjectImage(RetrieveDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = []
    lookup_field = 'project_slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        projectImages = ProjectImages.objects.filter(related_project_id=instance.id)
        projectImagesData = ProjectImageSerializer(projectImages, many=True).data
        return Response({'success': True, 'data': data, 'project_images': projectImagesData}, status=status.HTTP_200_OK)

