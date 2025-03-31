from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import EducationalResource, ForumPost, Comment, GenderStatistic, UserProfile
from .forms import ProfileForm, PostForm, CommentForm
import json
from django.core.serializers import serialize

def your_view(request):
    stats = YourModel.objects.all()
    stats_json = serialize('json', stats)
    return render(request, 'statistics.html', {'stats_json': stats_json})

def index(request):
    return render(request, 'equalifyApp/index.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create user profile
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'equalifyApp/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'equalifyApp/login.html', {'error': 'Invalid credentials'})
    return render(request, 'equalifyApp/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def dashboard(request):
    resources = EducationalResource.objects.all().order_by('-created_at')[:3]
    posts = ForumPost.objects.all().order_by('-created_at')[:3]
    stats = GenderStatistic.objects.all().order_by('-year')[:3]
    return render(request, 'equalifyApp/dashboard.html', {
        'resources': resources,
        'posts': posts,
        'stats': stats
    })

@login_required
def education(request):
    category = request.GET.get('category', '')
    if category:
        resources = EducationalResource.objects.filter(category=category)
    else:
        resources = EducationalResource.objects.all()
    return render(request, 'equalifyApp/education.html', {
        'resources': resources.order_by('-created_at'),
        'selected_category': category
    })

@login_required
def statistics(request):
    stats = GenderStatistic.objects.all().order_by('-year')
    return render(request, 'equalifyApp/statistics.html', {'stats': stats})

@login_required
def forum(request):
    posts = ForumPost.objects.all().order_by('-created_at')
    return render(request, 'equalifyApp/forum.html', {'posts': posts})

@login_required
def post_detail(request, post_id):
    post = ForumPost.objects.get(id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'equalifyApp/post_detail.html', {
        'post': post,
        'form': form
    })

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('forum')
    else:
        form = PostForm()
    return render(request, 'equalifyApp/create_post.html', {'form': form})

@login_required
def profile(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'equalifyApp/profile.html', {'form': form})