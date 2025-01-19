from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Post


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post/detail.html'
    context_object_name = 'post'

    def get_object(self):
        return get_object_or_404(
            Post,
            status=Post.Status.PUBLISHED,
            pub_date__year=self.kwargs['year'],
            pub_date__month=self.kwargs['month'],
            pub_date__day=self.kwargs['day'],
            slug=self.kwargs['post']
        )