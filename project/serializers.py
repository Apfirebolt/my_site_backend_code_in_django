from rest_framework import serializers
from . models import ProjectImages, Project


class ProjectSerializer(serializers.ModelSerializer):
    project_slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Project
        fields = ('project_name', 'project_url', 'project_description', 'project_technology', 'project_slug')


class ProjectImageSerializer(serializers.ModelSerializer):
    related_project_slug = serializers.SerializerMethodField()

    def get_related_project_slug(self, obj):
        return obj.related_project.project_slug

    class Meta:
        model = ProjectImages
        fields = ('project_image', 'related_project', 'image_description', 'related_project_slug',)