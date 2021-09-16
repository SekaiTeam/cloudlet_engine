from django.http import HttpResponseRedirect

def home(request):
    return HttpResponseRedirect("https://yamiokdl.github.io/CloudletEngineDocs/index.html")
