from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('education/', views.education, name='education'),
    path('statistics/', views.statistics, name='statistics'),
    path('forum/', views.forum, name='forum'),
    path('forum/post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('forum/create/', views.create_post, name='create_post'),
    path('profile/', views.profile, name='profile'),
]