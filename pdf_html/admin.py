from django.contrib import admin
from .models import Profile, patient_profile_conclusion

admin.site.register(Profile)
admin.site.register(patient_profile_conclusion)
