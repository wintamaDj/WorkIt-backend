from django.db import models
import users

class seeker_profile(models.Model):
    user = models.OneToOneField(users.User, on_delete=models.CASCADE)
    # pic = models.ImageField()
    # resume_doc = models.FileField()
