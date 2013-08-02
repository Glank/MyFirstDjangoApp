from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def detail(request, poll_id):
    return HttpResponse("detail: %s"%poll_id)

def results(request, poll_id):
    return HttpResponse("results: %s"%poll_id)

def vote(request, poll_id):
    return HttpResponse("vote: %s"%poll_id)
