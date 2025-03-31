from django.contrib import admin
from .models import UserProfile, EducationalResource, ForumPost, Comment, GenderStatistic

admin.site.register(UserProfile)
admin.site.register(EducationalResource)
admin.site.register(ForumPost)
admin.site.register(Comment)
admin.site.register(GenderStatistic)