# Only affects default Django admin site
from django.contrib import admin
from .models import User, Company, Seeker
from seeker.models import seeker_profile
from biz.models import company_profile

# Register your models here.
admin.site.register(User)
admin.site.register(Company)
admin.site.register(Seeker)

admin.site.register(seeker_profile)
admin.site.register(company_profile)