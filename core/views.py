from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post

def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    context = dict(
        posts = posts
    )

    return render(request, "core/frontpage.html", context)

def about(request):
    return render(request, "core/about.html")


def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type='text/plain')