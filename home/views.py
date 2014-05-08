from django.template import RequestContext
from django.shortcuts import render_to_response
# Create your views here.

def index(request):
	context = RequestContext(request)
	context_dict = {}

	return render_to_response('home/base.html', context_dict, context)
