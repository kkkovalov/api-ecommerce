from django.http import HttpResponse


def index(request):
    return HttpResponse('Website works, you earned a chocolate bar, to claim go to <a href="/docs/">/docs/</a>')