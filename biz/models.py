import datetime
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from authsite.models import User, Company
from seeker.models import user_reviews

# TO-DO:
# add slugs for profile???

# Create your models below

# profile
class company_profile(models.Model):
    # only-one and required
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(blank=True, upload_to='uploads/company/pic/')
    industry = models.CharField(blank=True, max_length=255)
    address = models.CharField(blank=True, max_length=255)
    contact = models.CharField(blank=True, max_length=255)

# Signaling to create profile
@receiver(post_save, sender=Company)
def create_company_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'COMPANY':
        company_profile.objects.create(user=instance)

# jobs
class company_jobs(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(blank=True, max_length=255)
    requirements = models.CharField(blank=True, max_length=255)
    open = models.BooleanField(default=False, help_text='TRUE is open, FALSE is closed')
    category = models.CharField(blank=True, max_length=255)

# apply
class job_applications(models.Model):
    PENDING = 'PDG'
    ACCEPT = 'ACC'
    REJECT = 'REJ'
    DEFAULT_EXPIRY = (datetime.date.today() + datetime.timedelta(days=31))

    JOB_STATUS = {
        PENDING: 'Pending',
        ACCEPT: 'Accepted',
        REJECT: 'Rejected',
    }

    # fields
    users = models.OneToOneField(User, on_delete=models.PROTECT)
    job = models.ForeignKey(company_jobs, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=JOB_STATUS, default=PENDING)
    expires = models.DateField(default=DEFAULT_EXPIRY)

    def responded(self):
        if not self.status == self.PENDING:
            self.expires = datetime.date.today() + datetime.timedelta(days=1)