from django.contrib import admin
from .models import Profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'fname',
        'lname',
        'technologies',
        'email',
        'display_picture'
    )
    
