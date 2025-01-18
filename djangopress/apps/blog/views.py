from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from .models import Post


def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    
    try:
        posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.get_page(paginator.num_pages)
    
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )

def post_detail(request, year, month, day, post):
    blog_post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        pub_date__year=year,
        pub_date__month=month,
        pub_date__day=day,
        slug=post
    )
    
    return render(
        request,
        'blog/post/detail.html',
        {'post': blog_post}
    )