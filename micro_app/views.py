from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello. You're at the Rndx App index page. <br><br><br><br><h2>Version 1</h2>")