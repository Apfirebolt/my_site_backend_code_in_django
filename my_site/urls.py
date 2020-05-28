from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from my_site import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='Homepage.html', extra_context={'jane': 12}), name='home'),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('gallery/', include(('gallery.urls', 'gallery'), namespace='gallery')),
    path('project/', include(('project.urls', 'project'), namespace='project')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
