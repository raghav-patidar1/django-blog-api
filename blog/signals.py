import os

from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from .models import Post


# Auto-delete image file from file system on deleting blog post
# instance
@receiver(post_delete, sender=Post)
def delete_associated_image(sender, instance, **kwargs):
    if instance.image_url:
        if os.path.isfile(instance.image_url.path):
            os.remove(instance.image_url.path)


# Auto-delete old image from file system when updating a blog post with a new
# image file
@receiver(pre_save, sender=Post)
def auto_delete_image_file_on_update(sender, instance, **kwargs):

    # New post instance, nothing to do.
    if not instance.pk:
        return

    try:
        old_image = Post.objects.get(pk=instance.pk).image_url
    except Post.DoesNotExist:
        return

    new_image = instance.image_url
    if not old_image == new_image:
        if old_image and os.path.isfile(old_image.path):
            os.remove(old_image.path)
