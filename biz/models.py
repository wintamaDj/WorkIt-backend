from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from root.models import User, Company

# TO-DO:
# setup default image
# add store image location
# add slugs for profile???

# Create your models here.
class company_profile(models.Model):
    # only-one and required
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # pic = models.ImageField(blank=True)
    pic = models.ImageField() # fix this later
    industry = models.CharField(max_length=255) 
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)

# Signaling to create profile
@receiver(post_save, sender=Company)
def create_company_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'COMPANY':
        company_profile.objects.create(user=instance)