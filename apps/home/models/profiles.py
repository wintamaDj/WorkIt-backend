from django.db import models
import users

class seeker_profile(models.Model):
    # only-one and required
    user = models.OneToOneField(users.User, on_delete=models.CASCADE)
    pic = models.ImageField(blank=True)
    resume = models.FileField(blank=True)

class company_profile(models.Model):
    # only-one and required
    user = models.OneToOneField(users.User, on_delete=models.CASCADE)
    pic = models.ImageField()
    industry = models.CharField(max_length=255) 
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)

class education_card(models.Model):
    # 0..*, many-to-one
    user = models.ForeignKey(users.User, on_delete=models.CASCADE)
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    date_start = models.DateField()
    date_end = models.DateField(blank=True, help_text='leave blank if still ongoing' )
    description = models.CharField(max_length=255, blank=True)

class user_timeline_jobs(models.Model):
    # 0..*, many-to-one
    useruser = models.ForeignKey(users.User, on_delete=models.CASCADE)
    jobtitle = models.CharField(max_length=255)
    employer = models.CharField(max_length=255)
    date_start = models.DateField()
    date_end = models.DateField()
    description = models.CharField(max_length=255)