from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import UserProfile, Post

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print('User registered:', user.username)  # Debug print
            login(request, user)
            return redirect('home')
        else:
            print('Form errors:', form.errors)  # Debug print
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def home(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    context = {
        'user_profile': user_profile
    }
    return render(request, 'home.html', context)


def upload_photo(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('photo_grid')  # Redirect to the photo grid page after successful upload
    else:
        form = PostForm()
    return render(request, 'upload_photo.html', {'form': form})

def photo_grid(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'photo_grid.html', {'posts': posts})
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/home/')  # Redirect to the desired page after successful login
        else:
            # Handle invalid login credentials
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})

    return render(request, 'login.html')
