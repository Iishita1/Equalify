from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('non-binary', 'Non-binary'),
        ('other', 'Other'),
        ('prefer-not-to-say', 'Prefer not to say')
    ])
    bio = models.TextField(blank=True)
    join_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.user.username

class EducationalResource(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100, choices=[
        ('education', 'Education Gap'),
        ('workplace', 'Workplace Equality'),
        ('leadership', 'Leadership Representation'),
        ('health', 'Health Disparities'),
        ('technology', 'Technology Gap')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title

class ForumPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

class GenderStatistic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    male_value = models.FloatField()
    female_value = models.FloatField()
    other_value = models.FloatField(null=True, blank=True)
    year = models.IntegerField()
    source = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title