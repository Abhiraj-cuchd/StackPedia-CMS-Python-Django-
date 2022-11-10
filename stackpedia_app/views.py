from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.utils.text import slugify
from django.contrib import messages

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'stackpedia_app/index.html', context)

def details_page(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.exclude(post_id=post.post_id)[:5]
    context = {
        'post': post,
        'posts' : posts
    }
    return render(request, 'stackpedia_app/details_page.html', context)

def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.save() 
            messages.info(request, 'Post created successfully')
            return redirect('create')
        else:
            messages.error(request, 'Oops!, Post not created')
    context = {'form': form}
    return render(request, 'stackpedia_app/create.html', context)

def updatePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.info(request, 'Post Updated successfully')
            return redirect('details_page', slug=post.slug)
        else:
            messages.error(request, 'Oops!, Post not Updated')
    context = {
        'form':form
    }
    return render(request, 'stackpedia_app/update.html', context)

def deletePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method == 'POST':
        post.delete()
        messages.info(request, 'Post Deleted successfully')
        return redirect('index')
    else:
        messages.error(request, 'Oops! Post not Deleted')
    context = {'form':form}
    return render(request, 'stackpedia_app/delete.html', context)