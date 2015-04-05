from django.shortcuts import render_to_response
from django.template import RequestContext

def homepage(request):
    return render_to_response('alpha/index.html', context_instance = RequestContext(request))

def index(request):
    return render_to_response('alpha/index.html', context_instance = RequestContext(request))

def industry(request):
    return render_to_response('alpha/inudstry.html', content_instance = RequestContext(request))

def getContactPage(request):
    return render_to_response('alpha/contact.html', context_instance = RequestContext(request))

def getBlogPage(request):
    return render_to_response('alpha/blog.html', context_instance = RequestContext(request))