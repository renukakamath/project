from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import ShortURLForm
from .models import ShortURL

def home(request):
    form = ShortURLForm(request.POST or None)
    short_url = None
    if request.method == "POST" and form.is_valid():
        short_instance = form.save()
        short_url = request.build_absolute_uri(f'/{short_instance.short_code}')
    return render(request, "shortener/home.html", {"form": form, "short_url": short_url})

def redirect_short_url(request, code):
    url_entry = get_object_or_404(ShortURL, short_code=code)
    return HttpResponseRedirect(url_entry.original_url)
