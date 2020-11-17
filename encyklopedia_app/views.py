from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.core.paginator import Paginator

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('nazwa')

    paginator = Paginator(posts,3)

    page = request.GET.get('page')

    posts = paginator.get_page(page)

    return render(request, 'encyklopedia_app/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'encyklopedia_app/post_detail.html', {'post': post})
