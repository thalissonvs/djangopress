from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
from .models import Post


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


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