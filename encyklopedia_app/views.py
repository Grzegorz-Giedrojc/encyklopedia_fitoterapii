from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def post_list(request):

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('nazwa')

    paginator = Paginator(posts,3)

    page = request.GET.get('page')

    posts = paginator.get_page(page)

    return render(request, 'encyklopedia_app/post_list.html', {'posts': posts})

def search(request):
    search_query = request.GET.get('search')
    if search_query:
        posts = Post.objects.filter(Q(nazwa__icontains = search_query) | Q(opis__icontains = search_query) | Q(choroby__icontains = search_query) | Q(zastosowanie__icontains = search_query))
        return render(request, 'encyklopedia_app/search.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'encyklopedia_app/post_detail.html', {'post': post})

def fitoterapia(request):
    return render(request, 'encyklopedia_app/fitoterapia.html', {})

def o_aplikacji(request):
    return render(request, 'encyklopedia_app/o_aplikacji.html', {})

def domowa_apteczka(request):
    return render(request, 'encyklopedia_app/domowa_apteczka.html', {})
