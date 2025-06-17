from statistics import mean
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from authsite.models import User, Seeker
from biz.models import company_jobs, job_applications

class seeker_profile(models.Model):
    # only-one and required
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(blank=True, upload_to='uploads/seeker/pic/')
    resume = models.FileField(blank=True, upload_to='uploads/seeker/resume/')

# Signaling to create profile
@receiver(post_save, sender=Seeker)
def create_seeker_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'SEEKER':
        seeker_profile.objects.create(user=instance)

class education_details(models.Model):
    # 0..*, many-to-one
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    date_start = models.DateField()
    date_end = models.DateField(blank=True, help_text='Leave blank if still ongoing')
    description = models.CharField(max_length=255, blank=True)

class user_timeline_jobs(models.Model):
    # 0..*, many-to-one
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jobtitle = models.CharField(max_length=255)
    employer = models.CharField(blank=True, max_length=255, help_text='use "self" if self-employed')
    date_start = models.DateField()
    date_end = models.DateField(blank=True, help_text='Leave blank if still ongoing')
    description = models.CharField(blank=True, max_length=255)

# # no logic to limit allow only hired employees
class user_reviews:
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_jobs_rel = models.ForeignKey(company_jobs, on_delete=models.CASCADE)
    job_application = models.ForeignKey(job_applications, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    # overall_rating = models.PositiveSmallIntegerField(max_length=5, default=0)
    benefits_rating = models.PositiveSmallIntegerField(max_length=5, default=0)
    life_balance_rating = models.PositiveSmallIntegerField(max_length=5, default=0)
    environment_rating = models.PositiveSmallIntegerField(max_length=5, default=0)
    opportunity_rating = models.PositiveSmallIntegerField(max_length=5, default=0)

    @property
    def avg_rating(self):
        benefit = self.benefits_rating
        life_bal = self.life_balance_rating
        environ = self.environment_rating
        oppty = self.opportunity_rating

        average = mean(benefit, life_bal, environ, oppty)
        
        return average