# Only affects default Django admin site
from django.contrib import admin
from .models.base_user import User, Company, Seeker
from .models.profiles import seeker_profile, company_profile

# Register your models here.
admin.site.register(User)
admin.site.register(Company)
admin.site.register(Seeker)

admin.site.register(seeker_profile)
admin.site.register(company_profile)