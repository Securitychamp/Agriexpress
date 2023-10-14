from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .models import Post, Category
from .forms import signupForm, loginForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def about(request):
    return render(request, 'about.html')


def guidelines(request):
    return render(request, 'Guidlines.html')


def currentissue(request):
    return render(request, 'current issue.html')


def article(request):
    return render(request, 'article.html')


def editorialboard(request):
    return render(request, 'editorial.html')


def contact(request):
    return render(request, 'contact.html')


def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = loginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                uid = authenticate(username=uname, password=upass)
                if uid is not None:
                    auth_login(request, uid)
                    messages.success(request, "logeed in sucessfully")
                    return HttpResponseRedirect("/profile")
                else:
                    form = loginForm()
                    return render(request, '/login.html', {'form': form})

        form = loginForm()
        return render(request, 'login.html', {'form': form})
    else:
        return HttpResponseRedirect("/profile")


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")


# blog/views.py

def category_posts(request, category_id):
    # Retrieve posts related to the given category_id
    category_posts = Post.objects.filter(category_id=category_id)

    # You can add additional context data or render a template as needed
    context = {
        'category_posts': category_posts,
    }
    return render(request, 'category_posts.html', context)


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, post_id):
    posts = Post.objects.get(pk=post_id)
    ver = Post.objects.all()
    all_categories = Category.objects.all()
    print("All Categories:", all_categories)
    return render(request, 'post_detail.html', {'post': posts, 'ver': ver, 'all_categories': all_categories})


def all_posts(request):
    # Retrieve all posts
    all_posts = Post.objects.all()

    # You can add additional context data or render a template as needed
    context = {
        'all_posts': all_posts,
    }
    return render(request, 'post_list.html', context)


# For user based post display:
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post, Author
from django.contrib.auth.models import User


def user_posts(request):
    # Fetch the 'Author' instance associated with the currently logged-in user
    author_instance = Author.objects.get(user=request.post)

    # Fetch posts associated with the 'Author' instance
    user_posts = Post.objects.filter(author=author_instance)

    return render(request, 'userpost.html', {'user_posts': user_posts})


# Create your views here.
def signup(request):
    if request.method == 'POST':
        fm = signupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Signup success")
            return redirect('/login')
    else:
        fm = signupForm()
    return render(request, 'signup.html', {'form': fm})


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return HttpResponseRedirect('/login')






from django.shortcuts import render

# Create your views here.
