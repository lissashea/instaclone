from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from instaapp.models import Post
from .models import UserProfile, Post, Comment
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserProfileSerializer, PostSerializer, CommentSerializer
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User

class ProfileView(View):
    def get(self, request):
        # Retrieve the currently logged-in user
        user = request.user

        # Retrieve the posts associated with the user
        posts = Post.objects.filter(user=user)

        # Create the context dictionary with user and posts
        context = {
            'user': user,
            'posts': posts,
        }

        # Render the profile.html template with the provided context
        return render(request, 'profile.html', context)

def profile(request):
    # Retrieve the currently logged-in user
    user = request.user

    # Retrieve the posts associated with the user
    posts = Post.objects.filter(user=user)

    # Create the context dictionary with user and posts
    context = {
        'user': user,
        'posts': posts,
    }

    # Render the profile.html template with the provided context
    return render(request, 'profile.html', context)

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

@login_required
def home(request):
    posts = Post.objects.filter(user=request.user)
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

@login_required
def photo_grid(request):
    posts = Post.objects.order_by('-created_at')
    context = {
        'posts': posts
    }
    return render(request, 'photo_grid.html', context)

def grid(request):
    posts = Post.objects.all()
    return render(request, 'grid.html', {'posts': posts})

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

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

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
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return Response(status=204)

@api_view(['DELETE'])
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return Response(status=204)

def create_comment(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        text = request.POST.get('text')  # Use 'text' instead of 'comment' to match the form field name
        if text:
            comment = Comment.objects.create(post=post, text=text, user=request.user)
            # Retrieve all comments for the post
            comments = post.comments.all()
            return render(request, 'grid.html', {'posts': Post.objects.all(), 'comments': comments})
        else:
            return redirect('grid')  # Handle the case when the 'text' variable is empty
    return redirect('grid')  # Or render an appropriate response in case of other request methods