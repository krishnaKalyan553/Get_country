from django.shortcuts import render
from django.http import HttpResponse
def home_view(request):
    country = getattr(request, 'country', None)
    if country == 'United States':
        html = "<html><body>yor are in United states </body></html>"
        return HttpResponse(html)
    elif country == 'India':
        html = "<html><body>yor are in India </body></html>"
        return HttpResponse(html)
    else:
        html = "<html><body>yor are not in India and Us </body></html>"
        return HttpResponse(html)