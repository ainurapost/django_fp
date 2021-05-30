from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
<<<<<<< HEAD
from .models import Post, Comment, Category
from .forms import LoginForm, RegisterForm, CommentForms
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q

=======
from .models import Post, Comment, Categories, Rate
from .forms import LoginForm, RegisterForm, CommentForms, NewPostForm, RatePostForm
from django.http import HttpResponseRedirect
>>>>>>> 1eb85dca06f7d85571f1f321a84ba3bfe0ba2c87


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
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    rate = 0
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
        r = Rate.objects.filter(post=pk).count()
        if r > 0:
            rate = post.rating_sum / r

        form = CommentForms()

    rate_form = RatePostForm()
    categories = Categories.objects.all()
    comments = Comment.objects.filter(post=pk)

    context = {
        'post': post,
        'form': form,
        'comments': comments,
        'rate': rate,
        'rate_form': rate_form,
        'categories': categories
    }
    return render(request, 'blog/view.html', context)


def rate(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    post = get_object_or_404(Post, id=pk)

    if request.method == 'POST':
        form = RatePostForm(request.POST)
        if form.is_valid():
            try:
                r = Rate(owner=request.user, post=post)
                r.save()
                post.rating_sum = post.rating_sum + form.cleaned_data['rating_sum']
                post.save()
            except BaseException as e:
                pass
    return HttpResponseRedirect(f'/view/{pk}/')


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
<<<<<<< HEAD

    query = request.GET.get('query')
    if query is None:
        return render(request, 'blog/search.html')

    res= Post.objects.filter(Q(title__icontains = query)|
                                 Q(text__icontains = query))
    print(query)
    print(res)
    return render(request, 'blog/search.html', {'res': res} )
=======

    if request.GET.get('query') is None:
        return render(request, 'blog/search.html')

    res = Post.objects.filter(Q(title__icontains=request.GET.get('query')) |
                              Q(clipped_text__icontains=request.GET.get('query')) |
                              Q(text__icontains=request.GET.get('query')))
    return render(request, 'blog/search.html', {'result': res})

>>>>>>> 1eb85dca06f7d85571f1f321a84ba3bfe0ba2c87


def add_post(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    fix_me = ""

    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = Post()
            post.owner = request.user
            post.title = form.cleaned_data['title']
            post.clipped_text = form.cleaned_data['clipped_text']
            post.text = form.cleaned_data['text']
            post.save()
            fix_me = "Запись успешно добавлена"
    else:
<<<<<<< HEAD
        form = LoginForm()
    return render(request, 'blog/add_post.html', {'form': form})
=======
        form = NewPostForm()

    return render(request, 'blog/add_post.html', {'form': form, 'msg': fix_me})
>>>>>>> 1eb85dca06f7d85571f1f321a84ba3bfe0ba2c87




def user(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    user = get_object_or_404(User, id=pk)
    posts = Post.objects.filter(owner = pk)
    context = {
        'user':user,
        'posts':posts,
    }
    return render(request, 'blog/user.html', context)


def error_404(request,exception):
    return render(request, 'blog/404.html')
