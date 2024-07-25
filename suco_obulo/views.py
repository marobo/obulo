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

    content = {
        'base_template': base_template,
        'posts': posts,
    }

    return render(request, 'index.html', content)


def list_aldeia_view(request):
    base_template = _base_template(request)

    context = {
        'base_template': base_template,
    }

    return render(request, 'suco_obulo/aldeia_list.html', context)


def detail_aldeia_view(request):
    base_template = _base_template(request)

    context = {
        'base_template': base_template,
    }

    return render(request, 'suco_obulo/aldeia_detail.html', context)
