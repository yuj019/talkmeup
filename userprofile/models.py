from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    displayName = models.CharField(max_length=100, blank=True, default='')
    createdOn = models.DateTimeField(auto_now_add=True)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.displayName

    class Meta:
        ordering = ('-createdOn',)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(owner=instance)
    instance.userprofile.save()
