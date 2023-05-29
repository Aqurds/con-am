from django.contrib import admin

from stories.models import StoryPage, StoryIndexPage


admin.site.register(StoryPage)
admin.site.register(StoryIndexPage)
