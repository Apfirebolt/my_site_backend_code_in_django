from django.db import models
from django.utils.text import slugify
from . choices import TECHNOLOGY_CHOICES


class Technology(models.Model):
    name = models.CharField('Technology Name', choices=TECHNOLOGY_CHOICES, max_length=200)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Technology"


class Project(models.Model):
    project_name = models.CharField("Project Name", max_length=250)
    project_description = models.TextField("Project Description")
    project_url = models.URLField("Project Url")
    project_technology = models.CharField("Project Technology", max_length=250)
    project_slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.project_slug = slugify(self.project_name)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.project_name)

    class Meta:
        verbose_name_plural = "Project"


class ProjectImages(models.Model):
    related_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    project_image = models.ImageField(upload_to='project_images')
    image_description = models.CharField("Image Description", max_length=250, default="No description available")

    def __str__(self):
        return str(self.related_project.project_url)

    class Meta:
        verbose_name_plural = "Project Images"