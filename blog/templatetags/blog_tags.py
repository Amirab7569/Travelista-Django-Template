from django import template
from blog.models import Post , Category
register = template.Library()

@register.simple_tag(name='posts')
def func():
    posts = Post.objects.filter(status=1).count()
    return posts


@register.simple_tag(name='show')
def func():
    posts = Post.objects.filter(status=1)
    return posts


@register.filter
def snippet(valu: str,args=20):
    return valu.upper()[:args] + '...'

@register.inclusion_tag('blog/blog-popular-post.html')
def latest_post(args=3):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:2]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def post_categories():
        posts = Post.objects.filter(status=1)
        categories = Category.objects.all()
        cat_dict = {}
        for name in categories:
            cat_dict[name]=posts.filter(category=name).count()
        
        return {'categories':cat_dict}