from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import home.models.base_user as base_user

class seeker_profile(models.Model):
    # only-one and required
    user = models.OneToOneField(base_user.User, on_delete=models.CASCADE)
    pic = models.ImageField(blank=True)
    resume = models.FileField(blank=True)

# Signaling to create profile
@receiver(post_save, sender=base_user.Seeker)
def create_seeker_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'SEEKER':
        seeker_profile.objects.create(user=instance)

class company_profile(models.Model):
    # only-one and required
    user = models.OneToOneField(base_user.User, on_delete=models.CASCADE)
    pic = models.ImageField()
    industry = models.CharField(max_length=255) 
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)

# Signaling to create profile
@receiver(post_save, sender=base_user.Company)
def create_company_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'COMPANY':
        company_profile.objects.create(user=instance)

# class education_card(models.Model):
#     # 0..*, many-to-one
#     user = models.ForeignKey(users.User, on_delete=models.CASCADE)
#     school = models.CharField(max_length=255)
#     degree = models.CharField(max_length=255)
#     field_of_study = models.CharField(max_length=255)
#     date_start = models.DateField()
#     date_end = models.DateField(blank=True, help_text='Leave blank if still ongoing')
#     description = models.CharField(max_length=255, blank=True)

# class user_timeline_jobs(models.Model):
#     # 0..*, many-to-one
#     useruser = models.ForeignKey(users.User, on_delete=models.CASCADE)
#     jobtitle = models.CharField(max_length=255)
#     employer = models.CharField(max_length=255)
#     date_start = models.DateField()
#     date_end = models.DateField(blank=True, help_text='Leave blank if still ongoing')
#     description = models.CharField(max_length=255)