from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, ListaZiol
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages


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
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Message from {form.cleaned_data["name"]}'
            message = form.cleaned_data["message"]
            recipients = ['grzesiekodkrywaja@gmail.com']
            try:
                send_mail(subject, message, 'giedrojc1012@wp.pl', ['grzesiekodkrywaja@gmail.com'], fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('o_aplikacji')

    return render(request, 'encyklopedia_app/o_aplikacji.html', {'form' : form})

def domowa_apteczka(request):
    ziolo = ListaZiol.objects.get(current_user=request.user)
    listazioll = ziolo.ziola.all()

    return render(request, 'encyklopedia_app/domowa_apteczka.html', {'listazioll' : listazioll})

def dodaj_ziolo(request, pk):
    post = get_object_or_404(Post, pk=pk)
    nowe_ziolo = Post.objects.get(pk=pk)
    ListaZiol.dodaj_ziolo(request.user, nowe_ziolo)
    messages.success(request, 'Dodano do apteczki')
    return render(request, 'encyklopedia_app/post_detail.html', {'post': post})

def usun_ziolo(request, pk):
    post = get_object_or_404(Post, pk=pk)
    nowe_ziolo = Post.objects.get(pk=pk)
    ListaZiol.usun_ziolo(request.user, nowe_ziolo)
    messages.info(request, 'Usunięto z apteczki')
    return render(request, 'encyklopedia_app/post_detail.html', {'post': post})
