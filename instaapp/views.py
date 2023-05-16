from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from rest_framework import serializers
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import UserProfile, Post, Comment
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import UserProfileSerializer, PostSerializer, CommentSerializer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    usernames = [user.username for user in users]
    return Response(usernames)

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
    
    # Add the 'user' object to the context
    context = {
        'form': form,
        'user': request.user  # Add the 'user' object to the context
    }
    return render(request, 'register.html', context)

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
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
    return render(request, 'home.html', {'posts': posts})  # Render the 'home.html' template instead of redirecting

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
    else:
        form = UserCreationForm()
    
    # Add the 'user' object to the context
    context = {
        'form': form,
        'user': request.user  # Add the 'user' object to the context
    }
    return render(request, 'login.html', context)

@api_view(['GET'])
def get_user_profile(request, user_id):
    user_profile = get_object_or_404(UserProfile, user_id=user_id)
    serializer = UserProfileSerializer(user_profile)
    return Response(serializer.data)

def get_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    serializer = PostSerializer(post)
    return Response(serializer.data)

@api_view(['GET'])
def get_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)

@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)  # Set the user of the post to the current authenticated user
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

def create_post_link(request):
    return redirect('upload_photo')

@api_view(['PUT'])
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    serializer = PostSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return Response(status=204)
