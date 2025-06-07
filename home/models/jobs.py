from django.db import models
import home.models.base_user as base_user

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