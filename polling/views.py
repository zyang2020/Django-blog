# polling/views.py
from django.shortcuts import render
from django.http import Http404
from polling.models import Poll

# Create your views here.
def list_view(request):
    # Poll.objects.all() will retrieve all objects from table 'Poll'.
    context = {'polls': Poll.objects.all()}
    # The render() function takes the 'request' object as its first argument,
    # a template name as its second argument and a 'dictionary' as its optional
    # third argument. It returns an HttpResponse object of the given template
    # rendered with the given context.
    return render(request, 'polling/list.html', context)

def detail_view(request, poll_id):
    try:
        # 'pk' is the prime key of the model (table). if we didn't specify it,
        # Django will automatically add an IntegerField to hold the primary key
        # Poll.objects.get() will retrieve a single object from the table "Poll"
        # with prime key = poll_id.
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404

    if request.method == "POST":
        # get the incomming data for "POST" req. method.
        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

    context = {'poll': poll}
    return render(request, 'polling/detail.html', context)
