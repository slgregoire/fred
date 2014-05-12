from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

import fred_graph

# Create your views here.

def index(request):
	context = RequestContext(request)
	chart = 0

	if request.method == 'POST':
		search_text = request.POST['query'].strip()
		
		chart = 1

		if search_text:
			fred_graph.fred_grapher(search_text)

	return render_to_response('graph/chart.html', {'chart': chart}, context)		



