from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Profile
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):

    if created:#if user is created now
        user = instance
        profile = Profile.objects.create(
            user=user,
            name=user.first_name,
            username=user.username,
            email=user.email,   
        )

@receiver(post_save, sender=Profile)
def updateUser(sender,instance,created, **kwargs):#will update User from Profile
    profile = instance
    user = profile.user

    if created == False:#if profile was already created
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


@receiver(post_delete, sender=Profile)# delete User if profile was deleted
def deleteUser(sender, instance, **kwargs):
    print('Deleting user')
    user = instance.user
    user.delete()


