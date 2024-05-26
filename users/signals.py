from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        # Check if the user has a profile before saving
        if hasattr(instance, 'profile'):
            instance.profile.save()
        else:
            # If the user doesn't have a profile, create one
            Profile.objects.create(user=instance)
