from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment, Category
from .forms import LoginForm, RegisterForm, CommentForms
from django.http import HttpResponseRedirect, HttpResponse



def index(request):
    post_list = Post.objects.all()
    categories= Category.objects.all()
    context = {'post_list': post_list,
               'title': 'Main page',
               'categories': categories,}
    return render(request, 'blog/index.html', context)


def get_category(request, category_id):
    post_list = Post.objects.filter(category_id=category_id)
    categories =Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'blog/category.html', {'post_list': post_list,
                                                  'categories': categories,
                                                  category: category}
                  )


def retrieve(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.views += 1
    post.save()
    if request.method == 'POST':
        form = CommentForms(request.POST)
        if form.is_valid():
            instance = Comment()
            instance.owner = request.user
            instance.post = post
            instance.text = form.cleaned_data['text']
            instance.save()
    else:
        form = CommentForms()

    comments = Comment.objects.filter(post=pk)

    context = {'post': post, 'form': form, 'comments': comments}
    return render(request, 'blog/view.html', context)


def reqister(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'],
                                            form.cleaned_data['email'],
                                            form.cleaned_data['password'])
            user.last_name = form.cleaned_data['lastName']
            user.first_name = form.cleaned_data['firstName']
            user.save()
    else:
        form = RegisterForm()

    return render(request, 'blog/register.html', {'form': form})


def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()

    return render(request, 'blog/login.html', {'form': form})


def search(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    query = request.GET.get('query')
    if not query:
        query = ""
        pass
    res= Post.objects.filter(title__icontains = query)
    print(query)
    print(res)

    return render(request, 'blog/search.html', {'res': res} )


def add_post(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'blog/add_post.html', {'form': form})


def user(request, pk):
    user = get_object_or_404(User, id=pk)
    posts = Post.objects.filter(owner = pk)
    context = {
        'user':user,
        'posts':posts,
    }
    return render(request, 'blog/user.html', context)


def error_404(request,exception):
    return render(request, 'blog/404.html')
