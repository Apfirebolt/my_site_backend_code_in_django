from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from . models import Project, ProjectImages, Technology
from . serializers import ProjectImageSerializer, ProjectSerializer, TechnologySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class ListTechnologyView(ListAPIView):
    serializer_class = TechnologySerializer
    queryset = Technology.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class CreateProject(CreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]


class ListProject(ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class CreateProjectImage(CreateAPIView):
    serializer_class = ProjectImageSerializer
    queryset = ProjectImages.objects.all()
    permission_classes = [IsAuthenticated]


class ListProjectImages(ListAPIView):
    serializer_class = ProjectImageSerializer
    queryset = ProjectImages.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class DetailProjectImage(RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectImageSerializer
    queryset = ProjectImages.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class UpdateDestroyProjectImage(RetrieveDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'project_slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        projectImages = ProjectImages.objects.filter(related_project_id=instance.id)
        projectImagesData = ProjectImageSerializer(projectImages, many=True).data
        return Response({'success': True, 'data': data, 'project_images': projectImagesData}, status=status.HTTP_200_OK)

