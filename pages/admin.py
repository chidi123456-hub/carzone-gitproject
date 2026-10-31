from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.

# create a class for team admin to be able to modify the admin layout
class TeamAdmin(admin.ModelAdmin):
    # create a function to render html tags and with all the objects
    def thumbnail(self,object):
        if not object.photo:
            return ""
    
        return format_html('<img src="{}" width="40" style="border-radius:50px;" />',object.photo.url,)
    
    # add a meaning name for thumbnail heading
    thumbnail.short_description = "Photo"

    # modification settings here
    list_display = ('id', 'thumbnail', 'first_name', 'last_name', 'designation', 'created_date')
    list_display_links =  ('id', 'thumbnail', 'first_name', 'designation')
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation',)

# include the model "team"
admin.site.register(Team, TeamAdmin)
