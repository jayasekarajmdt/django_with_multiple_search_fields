from django.contrib import admin

# Register your models here.
from .models import freelancer
from .models import skill

admin.site.register(freelancer)
admin.site.register(skill)