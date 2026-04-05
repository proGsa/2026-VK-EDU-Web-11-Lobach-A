from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    user_data = {
        'login': 'proGsa2026',
        'password': '1234',
    }
    return render(request, 'core/login.html', {'user': user_data})

def signup_view(request):
    user_data = {
        'login': 'proGsa2026',
        'email': 'nastya@lobach.info',
        'nickname': 'proGsa2026',
        'password': '1234',
        'password_repeat': '1234'
    }
    return render(request, 'core/signup.html', {'user': user_data})

def profile_view(request):
    user_data = {
        'username': 'proGsa2026',
        'email': 'nastya@lobach.info',
        'avatar_url': 'img/avatar.jpg',
        'nickname': 'proGsa2026',
        'rating': 1234,
        'join_date': '2024-01-15'
    }
    
    return render(request, 'core/profile.html', {'user': user_data})