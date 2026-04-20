from django.shortcuts import get_object_or_404, render

from .models import Post


def _base_template(request):

    if request.htmx:
        return 'base_site_htmx.html'
    return 'base_site.html'


def page(request, template_name, **kwargs):

    base_template = _base_template(request)
    posts = Post.objects.all().order_by('created_on')

    context = {
        'base_template': base_template,
        'posts': posts,
        **kwargs,
    }

    return render(request, template_name, context)


def post_detail_view(request, pk):

    base_template = _base_template(request)
    post = get_object_or_404(Post, pk=pk)

    context = {
        'base_template': base_template,
        'post': post,
    }
    return render(request, 'suco_obulo/post_detail.html', context)
