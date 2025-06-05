from django.db import models
import users

class company_jobs:
    users = models.ManyToOneRel(users.User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    requirements = models.CharField(max_length=255)

class user_reviews:
    company_jobs_rel = models.ManyToOneRel(company_jobs)
    rating = models.SmallIntegerField(max_length=5, default=5)
    description = models.CharField(max_length=255)

class user_applications:
    name = models.CharField(max_length=255)