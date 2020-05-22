from django.urls import path
from django.views.generic import TemplateView
from . views import CreateGalleryPost, ListGalleryPost, ContactMessageCreate, ContactMessageList


urlpatterns = [
    path('', TemplateView.as_view(template_name='gallery/gallery_home.html'), name='home'),
    path('create', CreateGalleryPost.as_view(), name='create-gallery'),
    path('list', ListGalleryPost.as_view(), name='list-gallery'),
    path('contact/list', ContactMessageList.as_view(), name='list-contact'),
    path('contact/create', ContactMessageCreate.as_view(), name='create-contact')
]