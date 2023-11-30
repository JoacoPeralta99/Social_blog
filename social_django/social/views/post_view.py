from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model 
from ..models import Post
from ..forms import UserRegisterForm , PostForm

def feed(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/feed.html',context)


def register(request):              # registro
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request , f'Usuario {username} creado')
            return redirect('feed')
    else:
        form = UserRegisterForm()
    
    context = {'form' : form }
    return render (request,'blog/register.html', context)


def post(request):
    current_user = get_object_or_404(get_user_model(), pk=request.user.pk)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user=current_user
            post.save()
            messages.success(request, 'Post enviado')
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'blog/post.html', {'form': form})




def profile(request, username= None):
    current_user = request.user
    if username and username != current_user.username:
        user = get_user_model().objects.get(username=username)
        posts = user.posts.all()

    else:
        posts = current_user.posts.all()
        user = current_user
    return render (request, 'blog/profile.html',{'user':user, 'posts':post})

