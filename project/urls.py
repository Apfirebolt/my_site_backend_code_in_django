from django.urls import path
from django.views.generic import TemplateView
from . views import (CreateProject, ListProject, ListProjectImages,
                     CreateProjectImage, UpdateDestroyProjectImage, DetailProjectImage)


urlpatterns = [
    path('', TemplateView.as_view(template_name='project/project_home.html'), name='home'),
    path('create', CreateProject.as_view(), name='create-project'),
    path('list', ListProject.as_view(), name='list-project'),
    path('image_create', CreateProjectImage.as_view(), name='create-project-image'),
    path('image_list', ListProjectImages.as_view(), name='list-project-image'),
    path('image_detail/<int:pk>', DetailProjectImage.as_view(), name='detail-project-image'),
    path('<str:project_slug>', UpdateDestroyProjectImage.as_view(), name='update-project-image')
]