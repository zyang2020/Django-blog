from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from blogging.models import Post
# Create your views here.

def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        #body += "\n".join(["\t%s" % a for a in args])
        body += "\n".join(["\t{}".format(a for a in args)])
    if kwargs:
        body += "Kwargs:\n"
        #body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
        body += "\n".join(["\t{}: {}".format(i for i in kwargs.items())])
    return HttpResponse(body, content_type="text/plain")

def list_view(request):
    # using QuerySet API to fetch all the posts that have been published.
    published = Post.objects.exclude(published_date__exact=None)
    # ordering the published posts by published_date descending using
    # QuerySet API order_by() method.
    # the hyphen line '-' means order descendingly.
    posts = published.order_by('-published_date')
    context = {'posts': posts}
    # NOTE: not using the render shortcut:
    #template = loader.get_template('blogging/list.html')
    #body = template.render(context)
    #return HttpResoonse(body, content_type='text/html')

    # NOTE: using the render shortcut:
    return render(request, 'blogging/list.html', context)
