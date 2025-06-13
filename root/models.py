from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

'''
### EXAMPLE ###
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
'''

# USER MODELS
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        SEEKER = 'SEEKER', 'Seeker'
        COMPANY = 'COMPANY', 'Company'

    # Sets default for registration
    base_role = Role.ADMIN
    
    # Adds new attribute 'role'
    role = models.CharField(max_length=50, choices=Role.choices)

    # Avoiding custom registration
    def save(self, *arg, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*arg, **kwargs)

# PROXY classes    
class Seeker(User):
    base_role = User.Role.SEEKER

    def print_fields(self):
        fields = self._meta.get_fields()
        for field in fields:
            print(field.name)

    class Meta:
        proxy = True

class Company(User):
    base_role = User.Role.COMPANY

    def print_fields(self):
        fields = self._meta.get_fields()
        for field in fields:
            print(field.name)

    class Meta:
        proxy = True