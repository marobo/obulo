from django.shortcuts import render

from .models import Post


def _base_template(request):

    if request.htmx:
        base_template = 'base_site_htmx.html'
    else:
        base_template = 'base_site.html'

    return base_template


def index(request):

    base_template = _base_template(request)
    posts = Post.objects.all().order_by('created_on')

    context = {
        'base_template': base_template,
        'posts': posts,
    }

    return render(request, 'index.html', context)


def aldeias_view(request):

    base_template = _base_template(request)
    posts = Post.objects.all().order_by('created_on')

    context = {
        'base_template': base_template,
        'posts': posts,
    }

    return render(request, 'suco_obulo/aldeias.html', context)


def nature_and_tourism_view(request):

    base_template = _base_template(request)
    posts = Post.objects.all().order_by('created_on')

    context = {
        'base_template': base_template,
        'posts': posts,
    }

    return render(request, 'suco_obulo/nature_and_tourism.html', context)


def people_and_culture_view(request):

    base_template = _base_template(request)
    posts = Post.objects.all().order_by('created_on')

    context = {
        'base_template': base_template,
        'posts': posts,
    }

    return render(request, 'suco_obulo/people_and_culture.html', context)
