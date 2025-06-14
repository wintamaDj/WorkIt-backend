from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from authsite.models import User, Seeker

class seeker_profile(models.Model):
    # only-one and required
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(blank=True)
    resume = models.FileField(blank=True)

# Signaling to create profile
@receiver(post_save, sender=Seeker)
def create_seeker_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'SEEKER':
        seeker_profile.objects.create(user=instance)

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
#     user = models.ForeignKey(users.User, on_delete=models.CASCADE)
#     jobtitle = models.CharField(max_length=255)
#     employer = models.CharField(max_length=255)
#     date_start = models.DateField()
#     date_end = models.DateField(blank=True, help_text='Leave blank if still ongoing')
#     description = models.CharField(max_length=255)


# WIP
# class company_jobs:
#     users = models.ForeignKey(users.User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     requirements = models.CharField(max_length=255)

# # no logic to limit allow only hired employees
# class user_reviews:
#     user = models.OneToOneField(users.User, on_delete=models.CASCADE)
#     company_jobs_rel = models.ForeignKey(company_jobs, on_delete=models.CASCADE)
#     rating = models.SmallIntegerField(max_length=5, default=5)
#     description = models.CharField(max_length=255)

# class user_job_form:
#     name = models.CharField(max_length=255)