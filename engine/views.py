from django.http import HttpResponseRedirect

def home(request):
    return HttpResponseRedirect("https://cloudletbot.ru/engine.html")
