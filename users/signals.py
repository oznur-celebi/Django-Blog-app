from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from.models import Profile, Bio

@receiver(post_save, sender =User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender =User)
def save_profile(sender, instance, **kwargs):
        instance.profile.save()


#bio
@receiver(post_save, sender =User)
def create_bio(sender, instance, created, **kwargs):
    if created:
        Bio.objects.create(user=instance)


@receiver(post_save, sender =User)
def save_bio(sender, instance, **kwargs):
       instance.bio.save()