from django.dispatch import receiver
from django.db.models.signals import post_save
from . models import BlogPost


@receiver(post_save, sender=BlogPost)
def update_blog_count(sender, instance, created, **kwargs):
    print('Instance is : ', instance)
    print('Sender is : ', sender)
    # instance.product.stock -= instance.amount
    # instance.product.save()


