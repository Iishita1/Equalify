from django import forms
from .models import UserProfile, ForumPost, Comment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['gender', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['title', 'content', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 6}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }