from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages
# Create your views here.

 
def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None :
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None :
        posts = posts.filter(author__username=kwargs['author_username'])  
    if kwargs.get('tag_name') != None :
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])  
        
        
    posts = Paginator(posts,3)
    try :
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid(): 
            form.save()
            messages.success(request,'your comment sucessfully submited')
        else:
            messages.error(request,'your comment didnt submited')
                    
    post = get_object_or_404(Post, pk=pid, status=1)
    comments = Comment.objects.filter(post=post.id,approved=1).order_by('-created_date')
    form = CommentForm()
    context = {'post':post,'comments':comments,'form':form}
    return render(request, 'blog/blog-single.html', context)

def test(request):
    return render(request, 'test.html')

def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_search(request):
    posts = Post.objects.filter(status=1) 
    if request.method == 'GET':
        if s:=request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)